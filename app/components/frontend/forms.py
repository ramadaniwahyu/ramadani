from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class CommentForm(FlaskForm):
    name = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    content = TextAreaField('Komentar', validators=[DataRequired()])
    submit = SubmitField('Simpan')

class ContactForm(FlaskForm):
    name = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    website = StringField('Website')
    content = TextAreaField('Konten', validators=[DataRequired()])
    submit = SubmitField('Kirim')