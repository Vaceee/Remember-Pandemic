import pymysql
from .. import db_result
from . import baseSelect


# 共4个函数


# 输入usr_no，获得对应password
#------------------------------------------------------------------
#   类  型：(str)
#   返回值：实例
#------------------------------------------------------------------
def getPassword(usr_no):
    record_name = ("usr_password")
    sql = '''
                SELECT usr_password
                FROM users
                WHERE usr_no = %s
                AND usr_enabled = 'Y'
        '''
    DR = db_result.DbResult(record_name,baseSelect(sql,(usr_no,)))
    return DR


# 输入usr_no，获得对应id
#------------------------------------------------------------------
#   类  型：(str)
#   返回值：实例
#------------------------------------------------------------------
def getUsrIdByUsrNo(usr_no) :
    record_name = ("usr_id")
    sql = '''
                SELECT id
                FROM users
                WHERE usr_no = %s
        '''
    DR = db_result.DbResult(record_name,baseSelect(sql,(usr_no,)))
    return DR


# 输入usr_no，获得对应userlevel
#------------------------------------------------------------------
#   类  型：(str)
#   返回值：实例
#------------------------------------------------------------------
def getUserLevel(usr_id):
    record_name = ("usr_userlevel")
    sql = '''
                SELECT usr_userlevel
                FROM users
                WHERE id = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql, (usr_id,)))
    return DR



# 对数据库中loginLogs进行insert操作（已检查）
#------------------------------------------------------------------
#   类  型：(int，str，datetime，str=“SJBBS”)
#   返回值：实例
#------------------------------------------------------------------
def loginLogsInsert(usr_id, login_ip, login_time, login_site = "SJBBS") :

    sql = '''
                INSERT INTO loginLogs(
                        usr_id,
                        login_ip,
                        login_time,
                        login_site
                ) VALUES (%s, %s, %s, %s)
        '''
    baseSelect(sql,(usr_id, login_ip, login_time, login_site))

    record_name = ("id")
    sql2 = '''
                SELECT id
                FROM loginLogs
                WHERE usr_id = %s
                ORDER BY
                        login_time DESC
                LIMIT 1
                OFFSET 0
        '''

    DR = db_result.DbResult(record_name, baseSelect(sql2, (usr_id,)))
    return DR



def forbidIPSelect(forbid_ip):
    record_name = ("count","time")
    sql1 = '''
                SELECT forbid_loginCnt, forbid_time FROM forbidIP
                WHERE forbid_ip = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql1,(forbid_ip,)))
    return DR


def forbidIPUpdate(forbid_ip, forbid_time):
    record_name = ("count","time")
    sql1 = '''
                REPLACE INTO forbidIP
                SET forbid_Cnt = forbid_Cnt+1, forbid_ip = %s, forbid_time = %s
        '''
    baseSelect(sql1,(forbid_ip, forbid_time))
    sql2 = '''
                SELECT forbid_ip, forbid_time FROM forbidIP
                WHERE forbid_ip = %s
        '''
    DR = db_result.DbResult(record_name, baseSelect(sql2,(forbid_ip,)))
    return DR


#新用户注册，插入users表
def Register(no, name, password, gender, register_time):
    record_name = ('usr_no')
    pre_sql='''
        SELECT usr_no FROM users
        WHERE usr_no = %s
    '''
    DR=db_result.DbResult(record_name, baseSelect(pre_sql, (no,)))
    if DR.size()!=0:
        return "REPEAT"

    sql='''
        INSERT INTO users(usr_no, usr_password, usr_name, usr_gender)
        VALUES (%s, %s, %s, %s)
    '''
    baseSelect(sql,(no, password, name, gender))

    DR=db_result.DbResult(record_name, baseSelect(pre_sql, (no,)))
    return DR
