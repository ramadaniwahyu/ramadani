from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):

    name = StringField('Nama', validators=[DataRequired()])
    url_name = StringField('URL')
    desc = TextAreaField('Keterangan')
    submit = SubmitField('Simpan')
