from flask import request, jsonify, Blueprint
import traceback
from ..glovar import *
from ..login_checker import loginRequired
from ..db_op import get_data as dg
from ..db_op import change_data as dc
from .. import tools


bseBp = Blueprint("search", __name__, url_prefix="/search")

@bseBp.route('', methods=['GET'])
@loginRequired
def search(**checkrst):
    try:
        data = request.get_json()
        text = data.get('text')
        order = data.get('order')
        limit = data.get('limit')
        if not text:
            return jsonify({'status': SEARCH_EMPTY})

        posts = dg.searchPosts(text, order=order, limit=limit).records()
        replies = dg.searchReplies(text, order=order, limit=limit).records()
        users = dg.searchUsers(text, limit=limit).records()
        return jsonify({'status': SEARCH_SUCCESS, 'posts': posts, 'replies': replies, 'users': users})
    except Exception:
        traceback.print_exc()
        return jsonify({'status': SEARCH_FAILED})


@bseBp.route('/hot', methods=['GET'])
@loginRequired
def searchHot(**checkrst):
    try:
        data = request.get_json()
        basId = data.get('bas_id')
        tagId = data.get('tag_id')
        limit = data.get('limit')
        print(basId, tagId, limit)
        hotPosts = dg.searchPosts_Hot(bas_id=basId, tag_id=tagId, limit=limit).records()
        return jsonify({'status': SEARCH_SUCCESS, 'hot_posts': hotPosts})
    except Exception:
        traceback.print_exc()
        return jsonify({'status': SEARCH_FAILED})