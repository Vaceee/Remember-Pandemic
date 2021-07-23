from flask import request, jsonify, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired
from ..db_op import get_data as dg
from ..db_op import change_data as dc
from .. import tools
import datetime
import traceback
from ..glovar import *

ntcBp = Blueprint('notices', __name__, url_prefix='/notices')

@ntcBp.route('/send',methods=['POST'])
@loginRequired
def noticeSend(**checkrst):
    try:
        data=request.get_json()
        ntc_content=data.get('content')
        if not ntc_content:
            return jsonify({'status':CONTENT_NULL})
        ntc_title=data.get('title')
        bas_id=data.get('bas_id')
        usr_from=checkrst['usr_id']
        #userlevel=dg.getUserProfile(usr_from).records()[0]['userlevel']
        check_auth=dg.checkAdmin(bas_id,usr_from)
        if check_auth.size()!=1:
            return jsonify({'status':NOTICE_NO_AUTHORIZE})
        ntc_time=datetime.datetime.now().replace(microsecond=0)
        result=dc.noticesInsert(bas_id,usr_from,ntc_content,ntc_time)
        if result.size()!=1:
            return jsonify({'status':NOTICE_FAILED})
        else:
            return jsonify({'status':NOTICE_SUCCESS})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':NOTICE_FAILED})


@ntcBp.route('/list', methods=['GET'])
@loginRequired
def noticeListDisplay(**checkrst):
    try:
        usr_id=checkrst['usr_id']
        notices=dg.getNotices(usr_id).records()
        #SELECT FIRST ... WHERE bas_id IN (SELECT bas_id FROM usr_class WHERE usr_id=usr_id) ORDER BY ntc_time DESC
        tools.standardizeNotices(notices) #{'bas_id':...,'bas_name':...,'last_title':...,'last_time':...}
        return jsonify({'status': GET_SUCCESS, 'notices': notices})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': NOTICE_FAILED})


@ntcBp.route('/detail',methods=['GET'])
@loginRequired
def noticeDetailDisplay(**checkrst):
    try:
        bas_id=request.get_json().get('bas_id')
        notices=dg.getClassNotices(bas_id).records()
        bas_name=dg.getClassProfile(bas_id).records()[0]['name']
        for ntc in notices:
            ntc['from']=dg.getUserProfile(ntc['usr_from']).records()[0]['name']
            ntc.pop('usr_from')
        return jsonify({'status': GET_SUCCESS, 'bas_name': bas_name, 'notices': notices})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':NOTICE_FAILED})
