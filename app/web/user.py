'''user模块注册用户相关的视图函数'''
from .import web
#
@web.route('/url')
def login():
    return 'hello1'
