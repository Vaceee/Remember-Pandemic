from flask import request, jsonify, make_response, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired, checkLimit
from ..jwt_op import generateJWT
from ..db_op import login as dl
from ..db_op import get_data as dg
from .. import tools
import time
import datetime
import traceback
from ..glovar import *

loginBp = Blueprint('login', __name__, url_prefix='/login')

# 功能：检查是否有过登陆、是否已过期
# 返回值：状态码及用户基本信息
@loginBp.route('', methods=['GET'])
@loginRequired
def loginCheck(**checkrst):
    try:
        info = dg.getUserProfile(checkrst['usr_id']).records()[0]
        response=make_response(jsonify({
            'status': GET_SUCCESS,
            'usr_no': info['usr_no'],
            'usr_name': info['name'],
            'usr_gender': info['gender'],
            'userlevel': info['userlevel']
        }))
        if checkrst.get('reset',False)==True:   #reset jwt when near expiration
            new_jwt=generateJWT(checkrst)
            max_age=60*60*24*3
            response.set_cookie('SJBBSID',new_jwt,max_age)
            print('Reset JWT')
        return response
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': LOGINOUT_UNKNOWN})


# 功能：接收学号密码，验证登录
# 返回值：状态码以及(登陆成功时)用户基本信息
@loginBp.route('', methods=['POST'])
def loginOperate():
    try:
        data=request.get_json()   # 把客户端的json表单转换为字典
        usr_no=data.get('usr_no')    #若键名存在，取得键值，否则返回None
        login_ip=request.remote_addr  #获取用户IP
        login_time=time.time()
        if not usr_no:
            exceeded=checkLimit(login_ip,login_time)
            if exceeded:
                return jsonify({'status':LIMIT_EXCEEDED})
            return jsonify({'status': NAME_NULL})

        usr_password=data.get('usr_password')
        if not usr_password:
            exceeded=checkLimit(login_ip,login_time)
            if exceeded:
                return jsonify({'status':LIMIT_EXCEEDED})
            return jsonify({'status': PASSWORD_NULL})

        password=dl.getPassword(usr_no)
        if password.size()!=1:  #查询不到密码或查询到密码多于一个
            exceeded=checkLimit(login_ip,login_time)
            if exceeded:
                return jsonify({'status':LIMIT_EXCEEDED})
            return jsonify({'status': LOGINOUT_UNKNOWN})
        elif usr_password != password.records()[0]['usr_password']:
            exceeded=checkLimit(login_ip,login_time)
            if exceeded:
                return jsonify({'status':LIMIT_EXCEEDED})
            return jsonify({'status': NAME_PASSWORD_WRONG})

        idResult =dl.getUsrIdByUsrNo(usr_no)   #通过学号获取id
        usr_id = idResult.records()[0]['usr_id']

        login_time=datetime.datetime.now().replace(microsecond=0)  #获取datetime时间
        dl.loginLogsInsert(usr_id,login_ip,login_time)  #将登陆记录插入数据库

        info=dg.getUserProfile(usr_id).records()[0]
        info['usr_id']=usr_id
        response=make_response(jsonify({
            'status': GET_SUCCESS,
            'usr_no': info['usr_no'],
            'usr_name': info['name'],
            'usr_gender': info['gender'],
            'userlevel': info['userlevel']
        }))  #response实例
        jwt=generateJWT(info)
        max_age=60*60*24*3   #过期时间为3天
        response.set_cookie('SJBBSID',jwt,max_age)
        return response
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': LOGINOUT_UNKNOWN})