from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)

# Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('config.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')
#app.config.from_object('config.TestingConfig')

Bootstrap(app)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"
migrate = Migrate(app, db)
ckeditor = CKEditor(app)

@app.route('/', methods=['GET', 'POST'])
def main():

    return redirect(url_for('frontend.main_home'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def dashboard():

    return render_template('dashboard.html', title='Beranda')

@app.route('/<path:resource>')
def serveStaticResource(resource):
	return send_from_directory('assets/', resource)

from .components.admin.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .components.admin.users import users as users_blueprint
app.register_blueprint(users_blueprint)

from .components.admin.categories import categories as categories_blueprint
app.register_blueprint(categories_blueprint)

from .components.admin.post import posts as post_blueprint
app.register_blueprint(post_blueprint)

from .components.admin.profile import profile as profile_blueprint
app.register_blueprint(profile_blueprint)

from .components.frontend import frontend as frontend_blueprint
app.register_blueprint(frontend_blueprint)

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Akses Ditolak'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Halaman Tidak Ditemukan'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Galat Server Internal'), 500