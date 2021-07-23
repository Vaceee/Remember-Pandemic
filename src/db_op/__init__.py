import pymysql
import traceback
from .. import db_result


__connect_auth = ("localhost","bbsmnger","sjbbs2019","bbsdb")


def baseSelect(sqlInput, tupleInput):
    db = pymysql.connect(*__connect_auth)
    cursor = db.cursor()

    try :
        cursor.execute(sqlInput, tupleInput) # 避免SQL注入攻击
        db.commit()
        returnValue = cursor.fetchall()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return
    finally :
        db.close()

    return returnValue




def baseSelectPlus(sqlInput, tupleInput):
    db = pymysql.connect(*__connect_auth)
    cursor = db.cursor()

    tupleLength = len(tupleInput)
    sqlLength = len(sqlInput)
    if(sqlLength != tupleLength):
        return

    returnValue = []

    for i in range(tupleLength):

        if(tupleInput[i]):
            # 元组为空时，条件表达式的值为False
            # 如果后面没有跟，那么就不需要tupleInput
            sql = sqlInput[i]
        else :
            sql = sqlInput[i] % tupleInput[i]


        try :
            cursor.execute(sql) # 尝试执行sql语句，每次都用try
            returnValue.append(cursor.fetchall()) # 因为元组没有append方法
        except :
            db.rollback() # 一旦有一次出错，事务回滚，全部撤销
            return

    try :
        db.commit() # 事件提交，已经在MySQL上测试了一致性
    except :
        db.rollback()
        return
    finally :
        db.close()
        return returnValue # 返回的是列表，不再是元组，
                           # 需要使用时自行用tuple函数处理（因为内部也是列表）


