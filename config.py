import os
from flask import current_app

class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = True
	TESTING = False
	TEMPLATES_AUTO_RELOAD = True
	PERMANENT_SESSION_LIFETIME = 600
	
	"""
	Database Connection
	"""
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user123:Q1w2e3r4!!@103.165.42.254/ramadani'
	# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user123:Q1w2e3r4!!@localhost/ramadani'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	BOOTSTRAP_FONTAWESOME = True
	SECRET_KEY = 'AFSBAKFBAKBFAK09876543TNJQN!$@y(!$yGABV'
	CSRF_ENABLED = True
 
	CKEDITOR_SERVE_LOCAL = True
	CKEDITOR_HEIGHT = 400
	CKEDITOR_ENABLE_CODESNIPPET = True
	CKEDITOR_FILE_UPLOADER = 'posts.upload'
	CKEDITOR_UPLOAD_ERROR_MESSAGE = 'Upload gagal'
	# CKEDITOR_ENABLE_CSRF = True
	# UPLOADED_PATH = os.path.abspath(current_app.root_path, 'assets/uploads') 
 
  

class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
