from flask import request, jsonify, make_response, Blueprint
from flask_cors import CORS
from ..db_op import login as dl
import datetime
import traceback
from ..glovar import *

registerBp = Blueprint('register', __name__, url_prefix='/register')

@registerBp.route('',methods=['POST'])
def register():
    try:
        data=request.get_json()   # 把客户端的json表单转换为字典
        no=data.get('usr_no')
        if not no:
            return jsonify({'status': NAME_NULL})
        name=data.get('usr_name')
        if not name:
            return jsonify({'status': NAME_NULL})
        password=data.get('usr_password')
        if not password:
            return jsonify({'status': PASSWORD_NULL})
        gender=data.get('usr_gender')
        if gender not in ('M','F'):
            gender='M'         #默认性别为男
        register_time=str(datetime.datetime.now())  #获取注册时间

        Rres = dl.Register(no, name, password, gender, register_time)
        #print(Rres)
        if Rres=='REPEAT':
            return jsonify({'status': NO_REPEAT})
        elif Rres.size()==1:
            return jsonify({'status': REGISTER_SUCCESS})
        else:
            return jsonify({'status' : REGISTER_FAIL})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'status' : REGISTER_FAIL})