from flask import request, jsonify, Blueprint
from flask_cors import CORS
from ..login_checker import loginRequired
from .. import tools
import traceback
from ..glovar import *

imgBp = Blueprint('image', __name__, url_prefix='/image')

@imgBp.route('/upload',methods=['POST'])
@loginRequired
def imageUpload(**chechrst):
    try:
        img=request.get_json().get('img') #base64
        if not img:
            return jsonify({'status':IMAGE_NULL})
        if (len(img)-22)*0.75/1024>2048:    #原始图片大小不超过2048KB
            return jsonify({'status':IMAGE_OVERSIZE})
        path = tools.saveImage(img)
        if not path:
            return jsonify({'status':IMAGE_FAILED})
        else:
            return jsonify({'status':IMAGE_SUCCESS, 'path':path})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'status':IMAGE_FAILED})