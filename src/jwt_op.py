import jwt
import time
from flask import Flask
import traceback

app = Flask(__name__)
app.config.from_object('config')
DAY_TIME=86400

def generateJWT(info):
    header={
        "typ":"JWT",
        "alg":"ES256"
    }
    payload = {
        "iss": "ofcourse.com",  #issuer
        "iat": time.time(),     #issue at
        "exp": time.time() + DAY_TIME*3,
        "usr_id": info['usr_id'],
        "level": info['userlevel']
    }
    private_key=app.config['PRIVATE_KEY']
    token = jwt.encode(payload, private_key, algorithm='ES256',headers=header).decode('utf8')
    return token

def checkJWT(token):
    try:
        public_key=app.config['PUBLIC_KEY']
        data=jwt.decode(token, public_key, algorithms='ES256')
        res={'is_login':1, 'usr_id':data['usr_id'], 'userlevel':data['level']}
        if data['exp']-time.time() < DAY_TIME:
            res.update({'reset':True})
        return res
    except jwt.ExpiredSignatureError:
        traceback.print_exc()
        return {'is_login': 0, 'expired': 1}
    except Exception as e:
        traceback.print_exc()
        return {'is_login': 0, 'expired': 0}
