import base64
import uuid
import time
from datetime import datetime
import traceback
import os
from .db_op import get_data as dg
from .db_op import change_data as dc
from .glovar import IMG_ROOT

'''
功能：获取特定页特定数量的帖子信息(按最后回帖时间排序)
参数：
    page 当前页数； limit 每页帖子数； sec_id 分栏id
返回值：
    字典的数组，每个字典对应一个帖子的信息
'''
def getPosts(page, limit, sec_id):
    top_num = dg.getTopCnt()  # 数据库中置顶帖的数量

    # dg.selectPosts(offset(从0计数), limit, whetherOnTop, sec_id)
    if top_num <= (page-1)*limit:  # 如果置顶帖已在前n-1页中显示完，则(当前)第n页都是非置顶贴
        posts = dg.selectPosts((page-1)*limit-top_num, limit, False, sec_id).records()
    else:  # 否则当前页第n页一定有置顶帖，可能有非置顶贴
        post1 = dg.selectPosts((page-1)*limit, min(top_num-(page-1)*limit, limit), True, sec_id).records()
        post2 = dg.selectPosts(0, max(page*limit-top_num, 0), False, sec_id).records()
        posts = post1 + post2

    return posts

'''
content规范化，<=30
last_time规范化，按照发帖时间选择时间格式
'''
def standardizePosts(posts):
    for each_post in posts:
        if len(each_post['content']) > 30:
            each_post['content'] = each_post['content'][:30]+'...'

        last_time = each_post['last_time']
        time_str = ''
        now_time = datetime.now()
        zero_time = datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0, 0)
        if last_time.year < now_time.year:  # 若发帖时间在今年之前，加上年份
            time_str += (str(last_time.year) + '-')
        if last_time < zero_time:  # 若发帖时间在今天零点之前，加上月份日期
            time_str += (str(last_time.month) + '-' + str(last_time.day) + ' ')
        time_str += last_time.strftime('%H:%M:%S')  # 显示时分秒
        each_post['last_time'] = time_str




'''
功能：获取指定页指定数量的回复
参数：page 当前页数； limit 每页帖子数； post_id 帖子id
返回：字典的数组，每个字典对应一个回复的信息
'''
def getReps(page, limit, post_id):
    replies=dg.selectRep(post_id,(page-1)*limit,limit)
    if replies.size() in range(limit+1):
        return replies.records()
    else:
        print("got unexpected number of replies when calling selectRep()")
        return None

def standardizeReplies(replies):
    for rep in replies:
        reply=dict()
        if rep['rep_cnt']==0:
            reply['first_reply']=None
        else:
            first_reply=dg.selectRepRep(rep['id'],offset=0,limit=1).records()[0]
            first_reply.pop('rep_cnt')
            reply['first_reply']=first_reply
        reply['reply_cnt']=rep.pop('rep_cnt')
        rep.update({'reply':reply})
    return


# usr_id: 请求方的 id
def standardizeMessages(messages, usr_id):
    for msg in messages:
        if usr_id==msg['usr_from']:
            name=dg.getUserProfile(msg['usr_to']).records()[0]['name']
            msg['usr_id']=msg['usr_to']
        elif usr_id==msg['usr_to']:
            name=dg.getUserProfile(msg['usr_from']).records()[0]['name']
            msg['usr_id']=msg['usr_from']
        msg['name']=name
        msg.pop('usr_from')
        msg.pop('usr_to')
        if len(msg['msg_content']) > 10:
            msg['msg_content'] = msg['msg_content'][:10]+'...'
        msg['last_content']=msg.pop('msg_content')
        last_time = msg.pop('msg_time')
        time_str = ''
        now_time = datetime.now()
        zero_time = datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0, 0)
        if last_time.year < now_time.year:
            time_str += (str(last_time.year) + '-')
        if last_time < zero_time:
            time_str += (str(last_time.month) + '-' + str(last_time.day) + ' ')
        time_str += last_time.strftime('%H:%M:%S')  # 显示时分秒
        msg['last_time'] = time_str
    return


def standardizeNotices(notices):
    for ntc in notices:
        bas_name=dg.getClassProfile(ntc['bas_id']).records()[0]['name']
        ntc['bas_name']=bas_name
        if len(ntc['ntc_content']) > 10:
            ntc['ntc_content'] = ntc['ntc_content'][:10]+'...'
        ntc['last_content']=ntc.pop('ntc_content')
        last_time = ntc.pop('ntc_time')
        time_str = ''
        now_time = datetime.now()
        zero_time = datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0, 0)
        if last_time.year < now_time.year:
            time_str += (str(last_time.year) + '-')
        if last_time < zero_time:
            time_str += (str(last_time.month) + '-' + str(last_time.day) + ' ')
        time_str += last_time.strftime('%H:%M:%S')  # 显示时分秒
        ntc['last_time'] = time_str
    return


#返回当前图片保存的路径
def getImgPath():
    path = IMG_ROOT
    localtime = time.localtime(time.time())
    year = localtime.tm_year
    month = localtime.tm_mon
    path += str(year) + '/'
    if month < 10:
        path += '0' + str(month)
    else:
        path += str(month)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


#raw_base64(str) 原base64字符串
#save_path(str) 图片保存路径，包含图片名称
def saveImage(raw_base64):
    img_format = ['jpg', 'png', 'jpeg', 'bmp', 'gif']
    save_path = None  # 出错时返回None
    img_data_bin = None
    try:
        for each_format in img_format:
            p = raw_base64.find(each_format, 0, 23)
            if p != -1:
                img_data_base64 = raw_base64[p+len(each_format)+8:]
                img_data_bin = base64.b64decode(img_data_base64)
                img_name = str(uuid.uuid1())  # 考虑用uuid作为图片名，保证名称唯一性
                path = getImgPath()
                save_path = path + '/' + img_name + '.' + each_format
                with open(save_path, 'wb') as file:
                        file.write(img_data_bin)
                break
        return save_path
    except Exception as e:
        traceback.print_exc()
        return save_path