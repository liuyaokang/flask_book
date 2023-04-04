'''蓝图初始化文件'''
from flask import Blueprint
web = Blueprint('web',__name__)

'''蓝图目录下导入flask'中的蓝图类,使用蓝图类创建一个web'''
from app.web import book
from app.web import user