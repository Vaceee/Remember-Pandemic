from flask import Flask
from flask_cors import CORS


app = Flask(__name__, static_folder="static",static_url_path="/static")

from .routes import (
    login, logout, register, messages, notices, posts, replies, sections, profile, image, search
)
app.register_blueprint(login.loginBp)
app.register_blueprint(logout.logoutBp)
app.register_blueprint(register.registerBp)
app.register_blueprint(messages.msgBp)
app.register_blueprint(notices.ntcBp)
app.register_blueprint(posts.postsBp)
app.register_blueprint(replies.repBp)
app.register_blueprint(sections.secBp)
app.register_blueprint(profile.profileBp)
app.register_blueprint(image.imgBp)
app.register_blueprint(search.bseBp)

CORS(app, supports_credentials=True)

from . import glovar


glovar.DEBUG = app.config['DEBUG']



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
