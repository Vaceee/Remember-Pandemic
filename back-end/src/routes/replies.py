from flask import request, jsonify, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired
from ..db_op import get_data as dg
from ..db_op import change_data as dc
from .. import tools
import datetime
import traceback
from ..glovar import *

repBp = Blueprint('replies', __name__, url_prefix='/replies')

#功能：接收帖子id、页数、每页帖子数，显示所有回复
#返回值：状态码，以及当前页面所有回复的id,content,time等有序json数组
@repBp.route('/fetch', methods=['GET'])
@loginRequired
def repliesDisplay(**checkrst):
    try:
        post_id=int(request.args.get('post_id'))
        page = int(request.args.get('page'))  #当前页数
        limit = int(request.args.get('limit'))  #每页帖子数
        rep_id=int(request.args.get('reply_id')) #-1表示请求post_id的回复，否则请求此rep_id的回复
        if rep_id==-1:
            replies=dg.selectPostRep(post_id,(page-1)*limit,limit).records()
        else:
            replies=dg.selectRepRep(rep_id,(page-1)*limit,limit).records()
        tools.standardizeReplies(replies)
        return jsonify({'status':GET_SUCCESS, 'replies': replies})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':REPLY_UNKNOWN})


#功能：发送回复
#返回值：状态码
@repBp.route('/new', methods=['POST'])
@loginRequired
def replyDeliver(**checkrst):
    try:
        data=request.get_json()
        rep_content=data.get('content')
        if not rep_content:
            return jsonify({'status':CONTENT_NULL})
        post_id=data['post_id']
        usr_id=checkrst['usr_id']
        rep_time=datetime.datetime.now().replace(microsecond=0)   #获取回复时间
        rep_to = data.get('rep_to',-1) # REVIEW:获取被回复对象的rep_id，若未指定则默认为回复帖子
        result=dc.repsInsert(usr_id,post_id,rep_content,rep_time,rep_to)
        if result.size()!=0:
            if rep_to==-1:
                dc.touchPost(rep_time,post_id)  #更新对应帖子的回复时间和回复总数
            else:
                dc.repedCntIncrease(rep_to)     #更新对应回复的被回复数
            return jsonify({'status':REPLY_SUCCESS})
        else:
            return jsonify({'status':REPLY_UNKNOWN})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':REPLY_UNKNOWN})


#功能：修改回复
#返回值：状态码
@repBp.route('/edit', methods=['POST'])
@loginRequired
def replyEdit(**checkrst):
    try:
        data=request.get_json()
        rep_id = data.get('id')
        verify = dg.checkRepStatus(rep_id)  #验证帖子信息
        if verify.size() == 0:
            return jsonify({'status': REPLY_UNEXIST})
        elif verify.size() != 1:
            return jsonify({'status': REPLY_UNKNOWN})
        elif verify.records()[0]['delete'] == 'Y':
            return jsonify({'status': REPLY_DELETED})

        usr_id = checkrst['usr_id']
        userlevel = dg.getUserProfile(usr_id).records()[0]['userlevel']  #得到用户等级
        if usr_id != verify.records()[0]['usr_id'] and userlevel != 1:  #该回复不是此用户发的 且 此用户不是管理员
            return jsonify({'status': REPLY_NO_AUTHORIZE})

        rep_content=data.get('content')
        if not rep_content:
            return jsonify({'status':CONTENT_NULL})

        rep_time=datetime.datetime.now()   #获取回复时间
        result=dc.repUpdate(rep_id,rep_content,rep_time)
        if result.size() == 1:
            return jsonify({'status':REPLY_SUCCESS})
        else:
            return jsonify({'status':REPLY_UNKNOWN})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':REPLY_UNKNOWN})


#功能：删除回复
#返回值：状态码
@repBp.route('/delete', methods=['POST'])
@loginRequired
def replyDelete(**checkrst):
    try:
        rep_id=request.get_json().get('id')
        verify = dg.checkRepStatus(rep_id)  #验证回复信息
        if verify.size() == 0:
            return jsonify({'status': REPLY_UNEXIST})
        elif verify.size() != 1:
            return jsonify({'status': REPLY_UNKNOWN})

        usr_id = checkrst['usr_id']
        userlevel = dg.getUserProfile(usr_id).records()[0]['userlevel']  #得到用户等级
        if usr_id != verify.records()[0]['usr_id'] and userlevel != 1:  #该回复不是此用户发的 且 此用户不是管理员
            return jsonify({'status': REPLY_NO_AUTHORIZE})

        result=dc.repDelete(rep_id)
        if result.size()==1 and result.records()[0]['delete']=='Y':
            return jsonify({'status':REPLY_SUCCESS})
        else:
            return jsonify({'status':REPLY_UNKNOWN})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':REPLY_UNKNOWN})



#功能：给某条回复点赞或取消赞
#返回值：状态码，以及该回复的被点赞数
@repBp.route('/like', methods=['POST'])
@loginRequired
def replyLike(**checkrst):
    try:
        method=request.get_json().get('method')   #str,"like" or "cancel"
        rep_id=request.get_json().get('rep_id')   #被点赞的回复id

        verify=dg.checkRepStatus(rep_id)
        if verify.size() == 0:
            return jsonify({'status': REPLY_UNEXIST})
        elif verify.size() != 1:
            return jsonify({'status': REPLY_UNKNOWN})
        elif verify.records()[0]['delete'] == 'Y':
            return jsonify({'status': REPLY_DELETED})

        usr_id=checkrst['usr_id']   #点赞者的id
        if method == 'like':
            add_result=dc.addlike(usr_id,rep_id)
            if add_result.size() != 1:
                return jsonify({'status':LIKE_FAILED})
            inc_result=dc.likeCntIncrease(rep_id)
            if inc_result.size() != 1:
                return jsonify({'status':LIKE_FAILED})
            like_cnt=inc_result.records()[0]['likecnt']    #操作后的点赞数
        elif method == 'cancel':
            can_result=dc.cancellike(usr_id,rep_id)
            if can_result.size() != 0:
                return jsonify({'status':LIKE_FAILED})
            dec_result=dc.likeCntDecrease(rep_id)
            if dec_result.size() != 1:
                return jsonify({'status':LIKE_FAILED})
            like_cnt=dec_result.records()[0]['likecnt']
        else:
            return jsonify({'status':LIKE_FAILED})
        return jsonify({'status':LIKE_SUCCESS, 'like_cnt':like_cnt})   #点赞或取消赞成功

    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':LIKE_FAILED})
