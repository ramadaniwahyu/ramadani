from flask import flash, redirect, render_template, url_for, request, session, current_app, app, send_from_directory
from flask_login import login_required, login_user, logout_user, current_user
from flask_ckeditor import upload_fail, upload_success
from . import posts
from ....models import Page
from .forms import PostForm, UploadForm
from werkzeug.utils import secure_filename
from .... import db
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
def random_uid():
    
    uid = secrets.token_hex(16)
    
    return uid

@posts.route('/admin/artikel', methods=['GET', 'POST'])
@login_required
def list():
    data = enumerate(Page.query.all(), start=1)
    
    return render_template('pages/list.html', data=data, title='Artikel')

@posts.route('/admin/artikel/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    new = False
    post = Page.query.get_or_404(id)
    form = PostForm(obj=post)
    form2 = UploadForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        db.session.add(post)
        db.session.commit()
        
        flash('Artikel telah diubah.')
        return redirect(url_for('posts.list'))
    
    elif form2.validate_on_submit():
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ext_type = filename.split('.')[-1]
            file_name = random_uid()
            storage_filename = str(file_name) + '.' +ext_type
            filepath = os.path.join(current_app.root_path, 'assets/img', storage_filename) 
            file.save(filepath)
            post.image = storage_filename
            db.session.commit()
            flash('Upload gambar berhasil')
            return redirect(url_for('posts.edit', id=post.id))
    
    form.title.data = post.title
    form.content.data = post.content
    form.category.data = post.category
    return render_template('pages/edit.html', post=post, form=form, new=new, form2=form2,title='Edit Artikel')

@posts.route('/admin/artikel/tambah', methods=['GET', 'POST'])
@login_required
def add():
    new = True
    form = PostForm()
    if form.validate_on_submit():
        page = Page(title=form.title.data, content=form.content.data, category=form.category.data, user_id=current_user.id)
        db.session.add(page)
        db.session.commit()
        
        flash('Artikel telah ditambahkan.')
        return redirect(url_for('posts.list'))
    return render_template('pages/edit.html', form=form, new=new, title='Tambah Artikel')

@posts.route('/admin/artikel/<id>/hapus', methods=['GET', 'POST'])
@login_required
def delete(id):
    page = Page.query.get_or_404(id)
    if page.image is not None :
        filepath = os.path.join(current_app.root_path, 'assets/img', page.image)
        os.remove(filepath)
    db.session.delete(page)
    db.session.commit()
    flash('Artikel telah dihapus.')
    return redirect(url_for('posts.list'))

@posts.route('/files/<filename>')
def uploaded_files(filename):
    path = os.path.join(current_app.root_path, 'assets/uploads')
    return send_from_directory(path, filename)
    
@posts.route('/upload', methods=['POST'])
@login_required
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Hanya gambar saja.')
    f.save(os.path.join(current_app.root_path, 'assets/uploads', f.filename))
    url = url_for('posts.uploaded_files', filename=f.filename)
    return upload_success(url, filename=f.filename)