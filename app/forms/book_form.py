from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired

class SearchForm(Form):
    '''数组可以传入多个校验对象'''
    q = StringField(validators=[DataRequired(),Length(min=1,max=99)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)

