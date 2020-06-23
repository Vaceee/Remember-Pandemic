from flask import request, jsonify, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired, adminRequired
from ..db_op import get_data as dg
from ..db_op import change_data as dc
from .. import tools
import datetime
import traceback
from ..glovar import *

postsBp = Blueprint('posts', __name__, url_prefix='/posts')

# 功能：接收页面、每页帖子数、分栏ID，显示帖子界面
# 返回值：状态码，以及当前页面所有贴子的id,title,content,name等有序json数组
@postsBp.route('/fetch', methods=['GET'])
@loginRequired
def postsDisplay(**checkrst):
    try:
        page = int(request.args.get('page'))  #当前页数
        limit = int(request.args.get('limit'))  #每页帖子数
        section_id = int(request.args.get('bas_id'))  #分栏ID
        posts=tools.getPosts(page,limit,section_id)
        tools.standardizePosts(posts)
        return jsonify({'status': GET_SUCCESS, 'posts': posts})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': POST_UNKNOWN})

# 功能：发送帖子
# 返回值：状态码
@postsBp.route('/new', methods=['POST'])
@loginRequired
def postDeliver(**checkrst):
    try:
        data = request.get_json()
        title = data.get('title')   #若键名存在，取得键值，否则返回None
        if not title:
            return jsonify({"status": TITLE_NULL})
        usr_id = checkrst['usr_id']
        quote_from = data.get('quote_from')
        content = data.get('content')
        bas_id = int(data['bas_id'])
        post_time = lastRepTime = datetime.datetime.now().replace(microsecond=0)  #发帖时间
        result = dc.postInsert(usr_id, title, content, post_time, lastRepTime, bas_id, quote_from)  #插入数据库
        if result.size() == 1:
            return jsonify({'status': POST_SUCCESS})
        else:
            return jsonify({'status': POST_UNKNOWN})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': POST_UNKNOWN})


# 功能：修改帖子
# 返回值：状态码
@postsBp.route('/edit', methods=['POST'])
@loginRequired
def postEdit(**checkrst):
    try:
        data = request.get_json()
        post_id = data.get('id')
        verify = dg.checkPostStatus(post_id)  #验证帖子信息
        if verify.size() == 0:
            return jsonify({'status': POST_UNEXIST})
        elif verify.size() != 1:
            return jsonify({'status': POST_UNKNOWN})
        elif verify.records()[0]['delete'] == 'Y':
            return jsonify({'status': POST_DELETED})

        usr_id = checkrst['usr_id']
        userlevel = dg.getUserProfile(usr_id).records()[0]['userlevel']  #得到用户等级
        if usr_id != verify.records()[0]['usr_id'] and userlevel != 1:  #该帖不是此用户发的 且 此用户不是管理员
            return jsonify({'status': POST_NO_AUTHORIZE})

        title = data.get('title')
        if not title:
            return jsonify({"status": TITLE_NULL})

        content = data['content']
        result = dc.postsUpdate(post_id, title, content)  #修改帖子
        if result.size() == 1:
            return jsonify({'status': POST_SUCCESS})
        else:
            return jsonify({'status': POST_UNKNOWN})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': POST_UNKNOWN})


# 功能：删除帖子
# 返回值：状态码
@postsBp.route('/delete', methods=['POST'])
@loginRequired
def postDelete(**checkrst):
    try:
        post_id=request.get_json().get('id')
        verify=dg.checkPostStatus(post_id)  #验证帖子信息
        if verify.size() == 0:
            return jsonify({'status': POST_UNEXIST})
        elif verify.size() != 1:
            return jsonify({'status': POST_UNKNOWN})
        usr_id=checkrst['usr_id']
        userlevel=dg.getUserProfile(usr_id).records()[0]['userlevel']
        if usr_id!=verify.records()[0]['usr_id'] and userlevel!=1: #该帖不是此用户发的 且 此用户不是管理员
            return jsonify({'status': POST_NO_AUTHORIZE})

        result=dc.postsDelete(post_id)
        if result.size()==1 and result.records()[0]['delete']=='Y':
            return jsonify({'status': POST_SUCCESS})
        else:
            return jsonify({'status': POST_UNKNOWN})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': POST_UNKNOWN})


# 功能：显示一个帖子
#返回值：状态码，以及此帖子的title,content等json串
@postsBp.route('/fetch-one', methods=['GET'])
@loginRequired
def postDisplayOne(**checkrst):
    try:
        post_id = request.args.get('post_id')
        one_post = dg.selectOnePost(post_id)
        if one_post.size() == 0:
            return jsonify({'status': POST_UNEXIST})
        elif one_post.size() != 1:
            return jsonify({'status': POST_UNKNOWN})
        one_post = one_post.records()[0]
        usr_id = one_post['usr_id']   #获取此帖发帖人的usr_id
        usr_name = dg.getUserProfile(usr_id).records()[0]['name']  #由usr_id得到usr_name
        one_post.pop('usr_id')  #删除返回值中不需要的usr_id
        one_post['usr_name'] = usr_name  #增添usr_name键值
        dc.postClicksIncrease(post_id)   #增加帖子点击数
        return jsonify({'status': GET_SUCCESS, 'post': one_post})   #帖子获取成功
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': POST_UNKNOWN})


#功能：合并某两条帖子
#返回值：状态码
@postsBp.route('/merge', methods=['POST'])
@loginRequired
@adminRequired
def postMerge(**checkrst):
    try:
        merge_from=request.get_json.get('merge_from') #被合并帖的id
        merge_to=request.get_json.get('merge_to') #向其合并的id
        verify = dg.checkPostStatus(merge_from)  #验证帖子信息
        if verify.size() == 0:
            return jsonify({'status': POST_UNEXIST})
        elif verify.size() != 1:
            return jsonify({'status': POST_UNKNOWN})
        elif verify.records()[0]['delete'] == 'Y':
            return jsonify({'status': POST_DELETED})

        result=dc.postMerge(merge_from, merge_to)
        if result.size()!=1:
            return jsonify({'status':MERGE_FAILED})
        elif result.records()[0]['merge_to']!=merge_to:
            return jsonify({'status':MERGE_FAILED})
        else:
            return jsonify({'status':MERGE_SUCCESS})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':MERGE_FAILED})