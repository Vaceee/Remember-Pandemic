from .. import db_result
import pymysql
import datetime
from . import baseSelect

# 共8个函数



# 对bbsdb.posts中置顶帖子数量进行计数（已检查）
#------------------------------------------------------------------
#   返回值：置顶帖数量（int）
#------------------------------------------------------------------
def getTopCnt() :
    sql = '''
            SELECT count(*)
            FROM posts
            WHERE post_onTop = \'Y\'
        '''
    topCnt = baseSelect(sql,())
    return topCnt[0][0]



# 查询Posts中几乎所有属性并返回（已检查）
#------------------------------------------------------------------
#   类  型：（int, int, bool, int）
#   返回值：实例
#------------------------------------------------------------------
def selectPosts(offset, limit, whetherOnTop, bas_id) :

    record_name = ('id', 'title', 'content', 'bas_id', 'on_top', 'rep_cnt', 'click_cnt', 'last_time', 'usr_name')
    sql = "SELECT posts.id, post_title, post_content, bas_id, post_onTop, post_repCnt, post_clickCnt, post_lastRepTime, usr_name \
           FROM users, posts \
           WHERE post_onTop ="+("'Y'" if whetherOnTop else "'N'")+"\
                 AND post_deleted = 'N' AND posts.usr_id = users.id " + ("AND bas_id = %s" if (bas_id != 0) else " ")+"\
           ORDER BY post_lastRepTime DESC \
           LIMIT %s OFFSET %s"
    if bas_id == 0 :
        selectPostsTuple = baseSelect(sql,(limit,offset))
    else :
        selectPostsTuple = baseSelect(sql,(bas_id,limit,offset))

    DR = db_result.DbResult(record_name,selectPostsTuple)

    return DR



# 根据id查询Posts中一条post并返回（已检查）
#------------------------------------------------------------------
#   类  型：（int）
#   返回值：对象，一大堆
#------------------------------------------------------------------
def selectOnePost(post_id):
    record_name = ("title","time","content","lastRepTime","quoteFrom","bas_id","usr_id","on_top")
    sql = '''
            SELECT  post_title,
                    post_time,
                    post_content,
                    post_lastRepTime,
                    post_quoteFrom,
                    bas_id,
                    usr_id,
                    post_onTop
            FROM posts
            WHERE id = %s
        '''

    DR = db_result.DbResult(record_name, baseSelect(sql, (post_id,)))
    return DR



# 根据post_id查询replies中若干条rep并返回
#------------------------------------------------------------------
#   类  型：（int）
#   返回值：对象，一大堆
#------------------------------------------------------------------
def selectPostRep(post_id, offset, limit):
    record_name = ("id", "usr_name", "content", "time", "like_cnt", "rep_cnt")
    sql = '''
            SELECT r.id, s.usr_name, r.rep_content, r.rep_time, r.rep_likeCnt, r.rep_repCnt
            FROM users AS s
            LEFT JOIN replies AS r
            ON s.id = r.usr_id
            WHERE r.post_id = %s AND r.rep_to = -1 AND r.rep_deleted = 'N'
            ORDER BY r.rep_time ASC
            LIMIT %s OFFSET %s
        '''
    # 当时为什么没加 ON？
    #print(sql) #temp added
    #print(post_id, limit, offset) #temp added
    DR = db_result.DbResult(record_name, baseSelect(sql, (post_id, limit, offset)))
    #print('DR.records():', DR.records())
    return DR


def selectRepRep(rep_id, offset, limit):
    record_name = ("id", "usr_name", "content", "time", "like_cnt", "rep_cnt")
    sql = '''
            SELECT replies.id, usr_name, rep_content, rep_time, rep_likeCnt, rep_repCnt
            FROM users LEFT JOIN replies
            ON users.id = replies.usr_id
            WHERE rep_to = %s AND rep_deleted = 'N'
            ORDER BY rep_time ASC
            LIMIT %s OFFSET %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql, (rep_id, limit, offset)))
    return DR


# 查询sections中几乎所有属性并返回（已检查）
#------------------------------------------------------------------
#   返回值：字典列表
#------------------------------------------------------------------
def getSectionInfo() :

    record_name = ("id","name","count", "comment", "forbidden", "star")
    sql = '''
            SELECT bas.id, bas.bas_name, bas.bas_postsCnt, bas.bas_comment,
                bas.bas_forbidden, bas.bas_star
            FROM base AS bas
        '''
    sectionTuple = baseSelect(sql,())
    DR = db_result.DbResult(record_name,sectionTuple)

    return DR



# REVIEW: 权限有关函数，其权限转至 admins 表中，此函数应当重写
#查找users中的name，gender，no，userlevel（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def getUserProfile(usr_id):
    record_name = ("name","gender","usr_no","userlevel")
    sql = '''
            SELECT usr_name,
                    usr_gender,
                    usr_no,
                    usr_userlevel
            FROM users
            WHERE id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql,(usr_id,)))
    return DR



# 查询posts是否被delete，还有id并返回（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def checkPostStatus(post_id):
    sql = '''
            SELECT post_deleted,
                    usr_id
            FROM posts
            WHERE id = %s
        '''
    record_name = ("delete","usr_id")

    DR = db_result.DbResult(record_name, baseSelect(sql, (post_id,)))
    return DR



# 查询replies是否被delete，还有id并返回（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def checkRepStatus(rep_id):
    sql = '''
            SELECT rep_deleted,
                    usr_id
            FROM replies
            WHERE id = %s
        '''
    record_name = ("delete","usr_id")

    DR = db_result.DbResult(record_name, baseSelect(sql, (rep_id,)))
    return DR



# 查询某个用户的所有消息列表
def getMessages(usr_id):
    record_names=("usr_from","usr_to","msg_time","msg_content")
    sql = '''
            SELECT usr_from,usr_to,msg_time,msg_content
            FROM messages AS msg1
            WHERE not exists (
                SELECT 1 FROM messages AS msg2
                WHERE (
                    (msg1.usr_from = msg2.usr_from AND msg1.usr_to = msg2.usr_to)
                    OR
                    (msg1.usr_from = msg2.usr_to AND msg1.usr_to = msg2.usr_from))
                AND msg1.msg_time < msg2.msg_time
            ) AND (msg1.usr_from = %s OR msg1.usr_to = %s)
            ORDER BY msg_time DESC
        '''
    DR = db_result.DbResult(record_names, baseSelect(sql, (usr_id,usr_id)))
    return DR


# 查询某两个用户的所有对话
def getChats(usr_from,usr_to):
    record_names=("usr_from", "usr_to", "msg_time", "msg_content")
    sql = '''
            SELECT usr_from, usr_to, msg_time, msg_content
            FROM messages
            WHERE (usr_from=%s AND usr_to=%s) OR (usr_from=%s AND usr_to=%s)
            ORDER BY msg_time ASC
        '''
    DR = db_result.DbResult(record_names, baseSelect(sql, (usr_from,usr_to,usr_to,usr_from)))
    return DR



# 查询某个用户的所有通知列表
def getNotices(usr_id):
    record_names=("bas_id","ntc_time","ntc_content")
    sql = '''
            SELECT bas_id,ntc_time,ntc_content
            FROM notices AS bas1
            WHERE bas_id IN (SELECT bas_id FROM usr_class WHERE usr_id = %s)
            AND NOT EXISTS(
                SELECT 1 FROM notices AS bas2
                WHERE bas1.bas_id = bas2.bas_id AND bas1.ntc_time < bas2.ntc_time
            )
            ORDER BY ntc_time DESC
        '''
    DR = db_result.DbResult(record_names, baseSelect(sql, (usr_id,)))
    return DR


# 查询某个班级的所有通知
def getClassNotices(cls_id):
    record_names=("usr_from","ntc_time","ntc_content")
    sql = '''
            SELECT usr_from, ntc_time, ntc_content
            FROM notices
            WHERE bas_id = %s
            ORDER BY ntc_time ASC
        '''
    DR = db_result.DbResult(record_names, baseSelect(sql, (cls_id,)))
    return DR


# 查询某个班级的详细资料
def getClassProfile(bas_id):
    record_names=(
        "name","no","grade","term", "comment", "forbidden", "postsCnt", "star",
    )
    sql = '''
            SELECT bas.bas_name, cls.cls_no, cls.cls_grade, cls.cls_term,
                bas.bas_comment, bas.bas_forbidden, bas.bas_postsCnt, bas.bas_star
            FROM base AS bas
            LEFT JOIN classes AS cls
            ON bas.id = cls.bas_id
            WHERE id = %s AND bas.bas_clsec = 'C'
        '''
    DR = db_result.DbResult(record_names, baseSelect(sql, (bas_id,)))
    return DR


# REVIEW: 由于权限系统，本函数可能在将来需要重写
# 查询某用户是否具有某班级的管理权限
def checkAdmin(usr_id,bas_id):
    record_name=("usr_id", "bas_id", "level", "delPst", "delRep", "lauNtc", "modNtc", "delNtc")
    sql = '''
            SELECT usr_id, bas_id, adm_level,
                adm_delPst, adm_delRep, adm_lauNtc, adm_modNtc, adm_delNtc
            FROM admins
            WHERE usr_id=%s AND bas_id=%s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql, (usr_id, bas_id)))
    return DR


# Search 相关：搜索有关贴子
def searchPosts(key, order="time", limit=None):
    def orderRepTime(sql):
        return sql + "ORDER BY pst.post_lastRepTime"
    def orderRepCnt(sql):
        return sql + "ORDER BY pst.post_repCnt"
    def orderClickCnt(sql):
        return sql + "ORDER BY pst.post_clickCnt"
    def limoffAppend(limit=None):
        return sql + (" LIMIT %s OFFSET 0" if limit is not None else " ")

    orderAppend = {
        'time': orderRepTime,
        'rep': orderRepCnt,
        'click': orderClickCnt,
    }


    record_name = ("id", "usr_name", "title", "content", "time", "repCnt", "clickCnt", "lastRepTime")
    sql = '''
            SELECT pst.id, usr.usr_name, pst.post_title, pst.post_content,
                pst.post_time, pst.post_repCnt, pst.post_clickCnt, pst.post_lastRepTime
            FROM posts AS pst
            LEFT JOIN users AS usr
            ON usr.id = pst.usr_id
            WHERE pst.post_deleted = 'N' AND (pst.post_content LIKE %s OR pst.post_title LIKE %s)
        '''
    if order in orderAppend:
        sql = orderAppend[order](sql)
    sql = limoffAppend(limit)
    res = baseSelect(
        sql, (('%'+key+'%', '%'+key+'%',) if limit is None
            else ('%'+key+'%', '%'+key+'%', limit,))
    )
    DR = db_result.DbResult (
            record_name, res
        )
    return DR

# Search 相关：搜索有关回复
def searchReplies(key, order='time', limit=None):
    def orderRepTime(sql):
        return sql + "ORDER BY rep.rep_time"
    def orderRepCnt(sql):
        return sql + "ORDER BY rep.rep_repCnt"
    def limoffAppend(limit=None):
        return sql + (" LIMIT %s OFFSET 0" if limit is not None else " ")

    orderAppend = {
        'time': orderRepTime,
        'rep': orderRepCnt,
    }

    record_name = ("id", "usr_name", "post_id", "content", "time", "repCnt")
    sql = '''
            SELECT rep.id, usr.usr_name, rep.post_id, rep.rep_content,
                rep.rep_time, rep.rep_repCnt
            FROM replies AS rep
            LEFT JOIN users AS usr
            ON usr.id = rep.usr_id
            WHERE rep.rep_deleted = 'N' AND rep.rep_content LIKE %s
        '''
    if key in orderAppend:
        sql = orderAppend[order](sql, limit=limit)
    sql = limoffAppend(limit)
    res = baseSelect(
        sql, (('%'+key+'%',) if limit is None
            else ('%'+key+'%', limit,))
    )
    DR = db_result.DbResult (
            record_name, res
        )
    return DR

# Search 相关：搜索有关用户
def searchUsers(key, order='no', limit=None):
    def orderUsrNo(sql):
        return sql + "ORDER BY usr.usr_no"
    def limoffAppend(limit=None):
        return sql + (" LIMIT %s OFFSET 0" if limit is not None else " ")

    orderAppend = {
        'no': orderUsrNo
    }

    record_name = ("no", "name", "grade", "gender")
    sql = '''
            SELECT usr_no, usr_name, usr_grade, usr_gender
            FROM users
            WHERE usr_enabled = 'Y' AND (
                usr_no LIKE %s OR usr_name LIKE %s
            )
        '''
    if key in orderAppend:
        sql = orderAppend[key](sql, limit=limit)
    sql = limoffAppend(limit)
    res = baseSelect(
        sql, ('%'+key+'%', '%'+key+'%',) if limit is None
            else ('%'+key+'%', '%'+key+'%', limit,)
    )
    DR = db_result.DbResult(
        record_name, res
    )
    return DR

# Search 有关 搜索（sec/cls，tag）热门贴子（未测试）

def searchPosts_Hot(bas_id=None, tag_id=None, limit=4):
    '''
    :param bas_id:  bas_id in {x|x in [1, inf], x in Z}
                    None -> return all tags of secs and clses.
                    else -> return posts in bas_id with all tags.

    :param tag_id:  tag_id in tags
                    None -> return all tags
                    else -> return posts with tag_id with all base.

    :param limit:   default = 4
                    else -> return the number of param limit.
    '''

    def basId(bas_id=None):
        id_notNone = {
            'join': (' LEFT JOIN base AS bas ON bas.id = pst.bas_id '),
            'where': (' AND bas.id = %s '),
            'format': (bas_id, )
        }
        id_None = {
            'join': ('  '),
            'where': ('  '),
            'format': ()
        }
        return id_notNone if bas_id is not None else id_None
    def tagId(tag_id=None):
        id_notNone = {
            'join': (
                ' LEFT JOIN post_tag AS ptg ON pst.id = ptg.post_id ',
                ' LEFT JOIN tags AS tg ON ptg.tag_id = tg.id ',
            ),
            'where': (
                ' AND tg.id = %s ',
            ),
            'format': (tag_id,)
        }
        id_None = {
            'join': ('  '),
            'where': ('  '),
            'format': ()
        }
        return id_notNone if tag_id is not None else id_None
    def limoff(limit=4):
        lim_notNone = {
            'limoff': ' LIMIT %s OFFSET 0 ',
            'format': (limit, )
        }
        lim_None = {
            'limoff': '  ',
            'format': ()
        }
        return lim_notNone if limit is not None else lim_None
    def cat(tupleIn):
        __st = ""
        for elem in tupleIn:
            __st += elem
        return __st

    bas = basId(bas_id=bas_id)
    tag = tagId(tag_id=tag_id)
    lim = limoff(limit=limit)
    sql = '''
            SELECT pst.id, usr.usr_name, pst.post_title, pst.post_content,
                pst.post_time, pst.post_repCnt, pst.post_clickCnt, pst.post_lastRepTime
            FROM posts AS pst
            LEFT JOIN users AS usr
            ON usr.id = pst.usr_id
        ''' + cat(bas['join']) + cat(tag['join']) + '''
            WHERE pst.post_deleted = 'N'
        ''' + cat(bas['where']) + cat(tag['where']) + '''
            ORDER BY (0.3 * pst.post_clickCnt + 0.7 * pst.post_repCnt)
            * EXP(0.27 * LOG10(NOW() - pst.post_time)) DESC
        ''' + lim['limoff']

    formatIn = bas['format'] + tag['format'] + lim['format']
    #print(sql, formatIn)
    res = baseSelect(sql, formatIn)
    record_name = ("id", "usr_name", "title", "content", "time", "repCnt", "clickCnt", "lastRepTime")
    DR = db_result.DbResult(record_name, res)
    return DR