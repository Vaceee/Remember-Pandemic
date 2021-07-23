from flask import jsonify, make_response, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired
import traceback
from ..glovar import *

logoutBp = Blueprint('logout', __name__, url_prefix='/logout')

# 功能：登出
# 返回值：状态码
@logoutBp.route('', methods=['GET'])
@loginRequired
def logoutOperate(**checkrst):
    try:
        response = make_response(jsonify({'status': GET_SUCCESS}))
        response.delete_cookie('SJBBSID')  #删除客户端cookie
        return response
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': LOGINOUT_UNKNOWN})