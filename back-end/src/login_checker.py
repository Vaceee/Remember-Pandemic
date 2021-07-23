from functools import wraps
from flask import jsonify, request
from .jwt_op import checkJWT
from .db_op import login as dl
from .db_op import get_data as dg
from .glovar import *
import traceback

# 参数类型：str
# 功能：检查到cookie，返回cookie字段；未检查到，返回None
def getCookie(ID):
    try:
        ck=request.cookies.get(ID)  #如果"ID"键存在，返回对应值，否则get()方法默认返回None
        return ck
    except Exception:
        traceback.print_exc()
        return None


# 装饰器
# 功能：用于所有登录状态下的操作，检查是否已登录或过期，
#      若有登录异常，返回异常信息，否则返回（执行）被装饰函数
def loginRequired(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        try:
            jwt=request.cookies.get('SJBBSID')
            if not jwt:
                return jsonify({'status':NOT_LOGIN})  #客户端没有cookie
            checkrst=checkJWT(jwt)  #dict
            if checkrst['is_login'] == 0:
                if checkrst['expired'] == 0:
                    return jsonify({'status':NOT_LOGIN})
                else:
                    return jsonify({'status':LOGIN_EXPIRED})
            kwargs.update(checkrst)
        except Exception:
            traceback.print_exc()
            return jsonify({'status':LOGINOUT_UNKNOWN})  #未知登录异常

        return func(*args, **kwargs)  #将checkrst传回被装饰函数
    return new_func

#装饰器：检查管理员权限
#备注：前提已成功登录？
def adminRequired(func):
    @wraps(func)
    def new_func(*args, **checkrst):  #**checkrst来自于loginRequired的返回
        try:
            usr_id=checkrst['usr_id']
            userlevel=dg.getUserProfile(usr_id).records()[0]['userlevel']
            if userlevel!=1:  #此用户不是管理员
                return jsonify({'status': POST_NO_AUTHORIZE})

        except Exception:
            traceback.print_exc()
            return jsonify({'status':POST_NO_AUTHORIZE})  #未知异常

        return func(*args, **checkrst)
    return new_func


def checkLimit(login_ip, login_time):
    logs=dl.forbidIPSelect(login_ip)
    if not logs.size():
        dl.forbidIPUpdate(login_ip,login_time)  #TRIGGER
    else:
        if logs.records()[0]['count']<10:
            dl.forbidIPUpdate(login_ip,login_time)
        elif login_time-logs.records()[0]['time']<TIMELIMIT:
            return jsonify({'status':LIMIT_EXCEEDED})
        else:
            dl.forbidIPUpdate(login_ip,login_time)
