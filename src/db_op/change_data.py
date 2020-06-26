import pymysql
from .. import db_result
from . import baseSelect

# 共14个函数


# 插入bbsdb.posts几乎全部属性并返回该插入项（未检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def postInsert(usr_id,post_title,post_content,post_time,post_lastRepTime,bas_id,post_quoteFrom,post_onTop='N'):
    sql = '''
        INSERT INTO posts(
            usr_id,
            post_title,
            post_content,
            post_time,
            post_quoteFrom,
            bas_id,
            post_onTop,
            post_lastRepTime
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    baseSelect(sql, (
        usr_id,
        post_title,
        post_content,
        post_time,
        post_quoteFrom,
        bas_id,
        post_onTop,
        post_lastRepTime
    ))
    sql2 = "SELECT id \
            FROM posts \
            WHERE usr_id = %s AND post_title = %s AND post_time = %s"

    record_name = ("post_id",)

    DR = db_result.DbResult(record_name, baseSelect(sql2,(usr_id, post_title, post_time)))
    return DR


def postCntIncrease(bas_id):
    record_name = ("bas_postsCnt")
    sql1 = '''
            UPDATE base
            SET bas_postsCnt = bas_postsCnt + 1
            WHERE id = %s
        '''
    baseSelect(sql1, (bas_id,))

    sql2 = '''
            SELECT bas_postsCnt
            FROM base
            WHERE id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2, (bas_id,)))
    return DR


# 更改posts的content或者title并返回该项（未检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def postsUpdate(post_id, post_title, post_content):
    sql = "UPDATE posts SET post_title = %s, \
                            post_content = %s \
                        WHERE id = %s"
    baseSelect(sql,(post_title, post_content, post_id))

    sql2 = "SELECT id, \
                   post_title,\
                   post_content \
            FROM posts \
            WHERE id = %s"
    record_name = ("post_id", "post_title", "post_content")

    DR =db_result.DbResult(record_name, baseSelect(sql2,(post_id,)))
    return DR



# 更改posts的delete项，并返回该项（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def postsDelete(post_id):
    sql = "UPDATE posts SET post_deleted = 'Y' WHERE id = %s"
    baseSelect(sql,(post_id))

    sql2 = '''
            SELECT post_deleted
            FROM posts
            WHERE post_deleted = 'Y' AND id = %s
        '''

    record_name = ("delete")

    DR = db_result.DbResult(record_name, baseSelect(sql2, (post_id,)))
    return DR






# 插入至bbsdb.images，根据source分支，并返回该插入项的img_id（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def imgInsert(img_title, img_path, source, id):
    record_name = ("id")
    #source有两种，“post”和“rep”，为str类型的参数
    if(source == "post"):
        sql = '''
            INSERT INTO images(
                    post_id,
                    img_title,
                    img_path
            ) VALUES(%s, %s, %s)
            '''
    elif(source == "rep"):
        sql = '''
            INSERT INTO images(
                    rep_id,
                    img_title,
                    img_path
            ) VALUES(%s, %s, %s)
            '''
    else :
        return ()
    baseSelect(sql, (id, img_title, img_path))

    sql2 = '''
            SELECT id
            FROM images
            WHERE img_path = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2, (img_path,)))

    return DR



# 根据post/rep的id，返回该贴子或回复下的所有图片的id（有疑问，不考虑传错source参数的情况吗）（而且这个应该写到get_data.py吧）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def imgsSelect(source, id):
    if source == 'post':
        sql = '''
            SELECT id
            FROM images
            WHERE post_id = %s
        '''
    else:
        sql = '''
            SELECT id
            FROM images
            WHERE rep_id = %s
        '''

    record_name = ('img_id',)
    DR = db_result.DbResult(record_name, baseSelect(sql, (id,)))
    return DR



# 根据img的id，删除该项，并返回该项的img_id，此时正常应为空元组
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def imgDelete(id):
    record_name = ("id")
    sql = '''
            DELETE
            FROM images
            WHERE id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql, (id,)))
    return DR






# 插入至bbsdb.replies，几乎包括全部属性，并返回该插入项
# 仅仅做回复插入工作
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def repsInsert(usr_id, post_id, content, time, to=-1):
    record_name = ("id", "post_repCnt", "rep_repCnt")
    sql1 = '''
            INSERT INTO replies(
                    usr_id,
                    post_id,
                    rep_to,
                    rep_content,
                    rep_time
            )VALUES(%s, %s, %s, %s, %s)
        '''
    baseSelect(sql1, (usr_id, post_id, to, content, time))

    sql2 = '''
            SELECT rep.id, pst.post_repCnt, rep.rep_repCnt
            FROM replies AS rep
            LEFT JOIN posts AS pst
            ON rep.post_id = pst.id
            WHERE rep.usr_id = %s
                AND pst.id = %s
                AND rep.rep_time = %s
        '''

    DR = db_result.DbResult(record_name, baseSelect(sql2, (usr_id, post_id, time)))
    return DR




# 做 rep 被回复数 rep_repCnt 增加操作
# 注：rep_to != -1 且 “回复操作” 针对 “回复” 而非 “贴子” 本身时（即：回复回复），才能使用本函数
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def repedCntIncrease(rep_to):
    record_name = ("rep_repCnt")
    sql1 = '''
            UPDATE replies
            SET rep_repCnt = rep_repCnt + 1
            WHERE id = %s
        '''
    baseSelect(sql1, (rep_to,))

    sql2 = '''
            SELECT rep_repCnt
            FROM replies
            WHERE id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2, (rep_to,)))
    return DR



# 更改replies几乎全部属性并返回该更改项id
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def repUpdate(rep_id, rep_content, rep_time):
    record_name = ("id")
    sql = '''
            UPDATE replies
            SET rep_content = %s,
                rep_time = %s
            WHERE id = %s
    '''

    baseSelect(sql, (rep_content, rep_time, rep_id))

    sql2 = '''
            SELECT id
            FROM replies
            WHERE id = %s
    '''
    DR = db_result.DbResult(record_name, baseSelect(sql2, (rep_id,)))
    return DR



# 根据id，更改replies中delete的值，并返回该项id（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def repDelete(rep_id):
    record_name = ("delete")
    sql1 = '''
            UPDATE replies
            SET rep_deleted = 'Y'
            WHERE id = %s
        '''
    sql2 = '''
            UPDATE replies AS r, replies AS rd
            SET rd.rep_repCnt = rd.rep_repCnt - 1
            WHERE r.id = %s AND r.rep_to = rd.id
        '''
    sql3 = '''
            UPDATE posts AS pst, replies AS rep
            SET pst.post_repCnt = pst.post_repCnt - 1
            WHERE rep.post_id = pst.id AND rep.id = %s
        '''
    baseSelect(sql1, (rep_id))
    baseSelect(sql2, (rep_id))
    baseSelect(sql3, (rep_id))

    sql4 = '''
            SELECT rep_deleted
            FROM replies
            WHERE id = %s
                AND rep_deleted = 'Y'
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql4, (rep_id,)))
    return DR






# 根据id，增加bbsdb.posts中对应贴子的点击量（已检查）
#------------------------------------------------------------------
#   返回值：无
#------------------------------------------------------------------
def postClicksIncrease(post_id):
    sql = '''
            UPDATE posts \
            SET post_clickCnt = post_clickCnt + 1
            WHERE id = %s
        '''
    baseSelect(sql, (post_id,))
    return



# 重置posts中对应贴子最后一次回复时间,并增加该贴repcnt数目，并返回（已检查）
# 完成回复与 “贴子” 之间的操作，包括总 repCnt 和 lastRepTime
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def touchPost(post_lastRepTime, post_id):

    sql1 = '''
            UPDATE posts \
            SET post_repCnt = post_repCnt + 1 \
            WHERE id = %s
        '''
    baseSelect(sql1, (post_id,))

    sql2 = '''
            UPDATE posts \
            SET post_lastRepTime = %s \
            WHERE id = %s
        '''
    baseSelect(sql2, (post_lastRepTime, post_id))

    sql3 = '''
            SELECT post_lastRepTime,
                    post_repCnt
            FROM posts
            WHERE id = %s
        '''
    record_name = ("time","repcnt")

    DR = db_result.DbResult(record_name, baseSelect(sql3,(post_id,)))

    return DR






# 插入至bbsdb.likes中，并返回该项（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def addlike(usr_id, rep_id):
    sql = '''
            INSERT INTO likes(
                rep_id,
                usr_id
            ) VALUES(%s, %s)
    '''
    baseSelect(sql, (rep_id, usr_id))

    record_name = ("rep_id", "usr_id")
    sql2 = '''
            SELECT rep_id,
                    usr_id
            FROM likes
            WHERE rep_id = %s
                AND usr_id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2, (rep_id, usr_id)))
    return DR



# delete操作 删除likes中的行，并返回（已检查）
#------------------------------------------------------------------
#   返回值：如果正确执行，应该返回()
#------------------------------------------------------------------
def cancellike(usr_id, rep_id):
    sql = '''
            DELETE
            FROM likes
            WHERE usr_id = %s
            AND rep_id = %s
        '''
    baseSelect(sql, (usr_id, rep_id))

    record_name = ("rep_id", "usr_id")
    sql2 = '''
            SELECT rep_id,
                    usr_id
            FROM likes
            WHERE rep_id = %s
            AND usr_id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2, (rep_id, usr_id)))
    return DR



# 将replies中likecnt属性的值增加1，并返回新值（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def likeCntIncrease(rep_id):
    sql1 = '''
            UPDATE replies
            SET rep_likeCnt = rep_likeCnt + 1
            WHERE id = %s
        '''
    baseSelect(sql1, (rep_id,))

    sql2 = '''
            SELECT rep_likeCnt
            FROM replies
            WHERE id = %s
        '''

    record_name = ("likecnt")
    DR = db_result.DbResult(record_name, baseSelect(sql2, (rep_id,)))
    return DR



# 将replies中likecnt属性的值减小1，并返回新值（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def likeCntDecrease(rep_id):
    sql1 = '''
            UPDATE replies
            SET rep_likeCnt = rep_likeCnt - 1
            WHERE id = %s
        '''
    baseSelect(sql1, (rep_id,))

    sql2 = '''
            SELECT rep_likeCnt
            FROM replies
            WHERE id = %s
        '''

    record_name = ("likecnt")
    DR = db_result.DbResult(record_name, baseSelect(sql2, (rep_id,)))
    return DR



# 将posts中post_mergedTo属性Update为新的id，并返回新值（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def mergePost(merge_from, merge_to):
    sql = '''
            UPDATE posts
            SET post_mergedTo = %s
            WHERE id = %s
        '''
    baseSelect(sql, (merge_to, merge_from))

    sql2 = '''
            SELECT post_mergedTo FROM posts
            WHERE id = %s
        '''
    record_name = ("merge_to")
    DR = db_result.DbResult(record_name, baseSelect(sql2, (merge_from)))
    return DR



# 将posts中post_mergedTo属性Update为0，并返回0
# （现在想来，有的时候不是修改合并的id，而是要取消合并）（已检查）
#------------------------------------------------------------------
#   返回值：实例
#------------------------------------------------------------------
def cancelMerge(post_id):
    sql = '''
            UPDATE posts
            SET post_mergedTo = 0
            WHERE id = %s
        '''
    baseSelect(sql, (post_id))

    sql2 = '''
            SELECT post_mergedTo FROM posts
            WHERE id = %s
        '''
    record_name = ("merge_to")
    DR = db_result.DbResult(record_name, baseSelect(sql2, (post_id)))
    return DR


# 将私信插入messages表
def messagesInsert(usr_from,usr_to,msg_content,msg_time):
    sql = '''
            INSERT INTO messages(usr_from,usr_to,msg_time,msg_content)
            VALUES(%s,%s,%s,%s)
        '''
    baseSelect(sql,(usr_from,usr_to,msg_time,msg_content))

    record_name=("id")
    sql2 = '''
            SELECT id FROM messages
            WHERE usr_from=%s AND usr_to=%s AND msg_time=%s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2,(usr_from, usr_to, msg_time)))
    return DR



# 将通知插入notices表
def noticesInsert(bas_id,usr_from,ntc_content,ntc_time):
    sql = '''
            INSERT INTO notices(bas_id,usr_from,ntc_content,ntc_time)
            VALUES(%s,%s,%s,%s)
        '''
    baseSelect(sql,(bas_id,usr_from,ntc_content,ntc_time))

    record_name=("id")
    sql2 = '''
            SELECT id FROM notices
            WHERE bas_id=%s AND usr_from=%s AND ntc_time=%s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2,(bas_id, usr_from, ntc_time)))
    return DR


def passwordUpdate(usr_id, password):
    sql = '''
            UPDATE users
            SET usr_password = %s
            WHERE id = %s
        '''
    baseSelect(sql, (password, usr_id))

    record_name=("usr_no")
    sql2 = '''
            SELECT usr_no FROM users
            WHERE id = %s AND usr_password = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2,(usr_id,password)))
    return DR



# print(postsUpdate(2,'aaa','5e3'))
# print(postsDelete(2))
# print(checkPostStatus(2))
# print(imgInsert('sda','ljg','post',1))
# print(imgDelete(1))
# repCntIncrement(2)
# print(repsInsert(3,1,'qss','2015-02-28 10:07:30'))
# print(repUpdate(1,'456','2019-02-21 19:13:20'))
# print(repDelete(1))
# print(touchPost('2019-02-21 19:13:20',1))
# print(addlike(2,1))
# print(likeCntIncrease(1))
# print(cancellike(2,1))
# print(likeCntDecrease(1))
# print(mergePost(1,2))