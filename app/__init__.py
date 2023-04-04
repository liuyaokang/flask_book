'''项目初始化文件,创建flask核心对象'''

from flask import Flask
from app.modles.book_model import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    from app.web.book import web
    from app.web.user import web
    app.register_blueprint(web)




