from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True) #设置为主键自增
    title = Column(String(50),nullable=False) #设置字符串字段长度以及是否为空
    author = Column(String(50),default='无名氏')
    isbn = Column(String(15),nullable=False,unique=True) #unique为True时不能重复
    binding = Column(String(20))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass

    
    

