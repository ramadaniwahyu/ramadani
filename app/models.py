from datetime import datetime, date, time
import uuid, secrets

from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr
# from sqlalchemy_utils import ScalarListType

from  app import db, login_manager

def random_uid():
    
    uid = secrets.token_hex(16)
    
    return uid


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.String(64), primary_key=True, default=random_uid)
    dibuat_pada = db.Column(db.DateTime, default=datetime.now)
    diubah_pada = db.Column(db.DateTime, onupdate=datetime.now)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class User(Base, UserMixin):
    name = db.Column(db.String(60))
    password_hash = db.Column(db.String(128))
    email =  db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)
    pages = db.relationship('Page', backref='user')

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password  
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '{}'.format(self.name)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))

class Category(Base):
    name = db.Column(db.String(60))
    url_name = db.Column(db.String(100))
    desc = db.Column(db.Text)
    pages = db.relationship('Page', backref='category')
    
    def __repr__(self):
        return '{}'.format(self.name)
    
class Comment(Base):
    page_id = db.Column(db.String(64), db.ForeignKey('page.id'))
    name = db.Column(db.String(60))
    email = db.Column(db.String(200))
    content = db.Column(db.Text())
    
    def __repr__(self):
        return '{}'.format(self.name)
    
page_tag = db.Table('page_tag',
    db.Column('tag_id', db.String(64), db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.String(64), db.ForeignKey('page.id'), primary_key=True)
)
    
class Tag(Base):
    name = db.Column(db.String(60))
    
    def __repr__(self):
        return '{}'.format(self.name)

class Page(Base):
    user_id = db.Column(db.String(64), db.ForeignKey('user.id'))
    category_id = db.Column(db.String(64), db.ForeignKey('category.id'))
    image = db.Column(db.String(200))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=page_tag, backref='pages')
    comments = db.relationship('Comment', backref='page')
    
    def __repr__(self):
        return '{}'.format(self.title)

class Contact(Base):
    name = db.Column(db.String(60))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(60))
    subject = db.Column(db.String(200))
    content = db.Column(db.Text())
    
    def __repr__(self):
        return '{}'.format(self.name)
    
class Profile(Base):
    site_title = db.Column(db.String(60))
    site_desc = db.Column(db.Text())
    profile_name = db.Column(db.String(200))
    profile_occupation = db.Column(db.String(200))
    profile_desc = db.Column(db.Text())
    slides = db.relationship('Slide', backref='profile')
    works = db.relationship('Work', backref='profile')
  
    def __repr__(self):
        return '{}'.format(self.site_title)
    
class Work(Base):
    profile_id = db.Column(db.String(64), db.ForeignKey('profile.id'))
    name = db.Column(db.String(60))
    icon = db.Column(db.String(200))
    desc = db.Column(db.Text())
  
    def __repr__(self):
        return '{}'.format(self.name)
    
class Slide(Base):
    profile_id = db.Column(db.String(64), db.ForeignKey('profile.id'))
    name = db.Column(db.String(200))
  
    def __repr__(self):
        return '{}'.format(self.name)