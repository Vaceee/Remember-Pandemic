from flask import request, jsonify, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired
from ..db_op import login as dl
from ..db_op import get_data as dg
from ..db_op import change_data as dc
from .. import tools
import datetime
import traceback
from ..glovar import *

msgBp = Blueprint('messages', __name__, url_prefix='/messages')

@msgBp.route('/send',methods=['POST'])
@loginRequired
def messageSend(**checkrst):
    try:
        data=request.get_json()
        msg_content=data.get('content')
        if not msg_content:
            return jsonify({'status':CONTENT_NULL})
        usr_from=checkrst['usr_id']
        usr_to=data['usr_to']
        #usr_to_no=data['usr_to_no']    #depend on what data front-end can provide
        msg_time=datetime.datetime.now().replace(microsecond=0)
        print(usr_from, usr_to, msg_content, msg_time)
        result=dc.messagesInsert(usr_from,usr_to,msg_content,msg_time)
        if result.size()!=1:
            return jsonify({'status':MESSAGE_FAILED})
        else:
            return jsonify({'status':MESSAGE_SUCCESS})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':MESSAGE_FAILED})


@msgBp.route('/list', methods=['GET'])
@loginRequired
def messageListDisplay(**checkrst):
    try:
        usr_id=checkrst['usr_id']
        messages=dg.getMessages(usr_id).records()
        tools.standardizeMessages(messages, usr_id) #{'usr_id':...,'name':...,'last_content':...,'last_time':...}
        return jsonify({'status': GET_SUCCESS, 'messages': messages})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': MESSAGE_FAILED})


@msgBp.route('/chat',methods=['GET'])
@loginRequired
def messageChatDisplay(**checkrst):
    try:
        usr_from=checkrst['usr_id']
        usr_to=request.get_json().get('usr_to')    #depend on what data front-end can provide
        messages=dg.getChats(usr_from,usr_to).records()
        return jsonify({'status': GET_SUCCESS, 'messages': messages})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':MESSAGE_FAILED})
