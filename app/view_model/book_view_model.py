'''用来加工api获取的数据，使其对应上数据库表的设计'''
class BookViewModel():
    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'books':[], #存储所有书籍的信息
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls._cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books': [],  # 存储所有书籍的信息
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def _cut_book_data(cls,data): #用来获取一本书的详细信息
        book={
            'title':data['title'],
            'publisher':data['publisher'],
            'page':data['pages'] or '',
            'author':'、'.join(data['author']),  #join函数用来连接列表的每一项
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book