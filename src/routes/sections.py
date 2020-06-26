from flask import jsonify, Blueprint
from ..login_checker import loginRequired
from ..db_op import get_data as dg
import traceback
from ..glovar import *

secBp = Blueprint('sections', __name__, url_prefix='/sections')

# 功能：展示分栏信息
# 返回值：每一栏的id,name,count的json数组
@secBp.route('/fetch', methods=['GET'])
@loginRequired
def sectionDisplay(**checkrst):
    try:
        #print(dg.getSectionInfo().records())
        return jsonify({'status': POST_SUCCESS, 'sections': dg.getSectionInfo().records()})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': POST_UNKNOWN})