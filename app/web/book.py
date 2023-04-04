from flask import jsonify,request
from app.libs.helper import is_isbn_or_key
from app.libs.search import Yushubook
from . import web
from app.forms.book_form import SearchForm
from app.view_model.book_view_model import BookViewModel
@web.route("/search")
def search():
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args) #request.args可以获取路由传递过来的数据
    if form.validate():
        '''validate为true的时候验证通过 '''
        q = form.q.data.strip()
        page = form.page.data
        '''从form里取值可以取到验证层的默认值，从request.args里取值如果客户端没传则为空值 '''
        isbn_or_key= is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            code = Yushubook.search_by_isbn(q)
            code = BookViewModel.package_single(code,q)
        else:
            code = Yushubook.search_by_keyword(q,page)
            code = BookViewModel.package_collection(code,q)
        return jsonify(code)
    else:
        return jsonify(form.errors)