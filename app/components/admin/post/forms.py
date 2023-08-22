from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileField, FileAllowed

from ....models import Category

class PostForm(FlaskForm):
    category = QuerySelectField('Kategori', query_factory=lambda: Category.query.all(), get_label='name', allow_blank=True)
    title = StringField('Judul', validators=[DataRequired()])
    content = CKEditorField('Konten')
    submit = SubmitField('Simpan')

class UploadForm(FlaskForm):
    image = FileField('Upload Gambar', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'File gambar saja')])
    submit2 = SubmitField('Simpan')
    
class ContactForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone')
    email = StringField('Email', validators=[Email()])
    subject = StringField('Subject')
    content =  StringField('Messages')
    submit = SubmitField('Send Message')