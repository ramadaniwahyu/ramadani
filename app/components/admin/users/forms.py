from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class UserForm(FlaskForm):

    name = StringField('Nama Pengguna', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField('Centang bila pengguna sebagai administrator.')
    submit = SubmitField('Simpan')

# class PenggunaForm(FlaskForm):
#     name = StringField('Nama Pengguna', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     foto = FileField('Upload Foto', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'File gambar saja')])
#     submit = SubmitField('Simpan')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Password Lama', validators=[DataRequired()])
    password = PasswordField('Password Baru', validators=[DataRequired()])
    confirm_password = PasswordField('Konfirmasi Password Baru', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Ganti Password')