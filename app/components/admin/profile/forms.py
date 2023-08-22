from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):

    site_title = StringField('Nama Situs', validators=[DataRequired()])
    site_desc = TextAreaField('Deskripsi Situs', validators=[DataRequired()])
    profile_name = StringField('Nama Profil', validators=[DataRequired()])
    profile_occupation = StringField('Pekerjaan', validators=[DataRequired()])
    profile_desc = TextAreaField('Deskripsi Profil', validators=[DataRequired()])
    submit1 = SubmitField('Simpan')
    
class WorkForm(FlaskForm):

    name = StringField('Nama', validators=[DataRequired()])
    icon = StringField('Icon', validators=[DataRequired()])
    desc = TextAreaField('Deskripsi', validators=[DataRequired()])
    submit2 = SubmitField('Simpan')
    
class SlideForm(FlaskForm):

    name = StringField('Teks', validators=[DataRequired()])
    submit3 = SubmitField('Simpan')