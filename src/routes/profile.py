from flask import request, jsonify, make_response, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired, checkLimit
from ..jwt_op import generateJWT
from ..db_op import change_data as dc
from .. import tools
import time
import datetime
import traceback
from ..glovar import *

profileBp = Blueprint('profile', __name__, url_prefix='/profile')

@profileBp.route('/setpassword', methods=['POST'])
@loginRequired
def setPassword(**checkrst):
    try:
        pswd=request.get_json().get('password')
        if not pswd:
            return jsonify({'status':PASSWORD_NULL})
        usr_id=checkrst['usr_id']
        res=dc.passwordUpdate(usr_id,pswd)
        if res.size()!=1:
            return jsonify({'status':SET_FAILED})
        response=make_response(jsonify({'status':SET_SUCCESS}))
        response.delete_cookie('SJBBSID')
        return response
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':SET_FAILED})