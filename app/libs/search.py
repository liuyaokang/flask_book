from app.libs.http_test import Http
from flask import current_app

class  Yushubook:
    # per_page =15
    isbn_url ="http://t.talelin.com/v2/book/isbn/{}"
    ''' 根据isbn的搜索方式'''
    keyword_url= 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'
    '''根据关键字的搜索方式'''

    def __init__(self):
        self.total = 0
        self.books = []


    def search_by_isbn(self,isbn):
        url=Yushubook.isbn_url.format(isbn)
        result =Http.get(url)
        return result


    def search_by_keyword(self,keyword,page=1):
        url=Yushubook.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        result =Http.get(url)
        return result

    def __file__single(self,data):
        self.total =1
        self.books.append(data)

    def __file__collection(self,data):
        pass

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']