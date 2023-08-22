from flask import flash, redirect, render_template, url_for, request, session, app
from flask_login import login_required, login_user, logout_user, current_user
from . import users
from ....models import User
from .forms import UserForm, ChangePasswordForm
from .... import db

@users.route('/admin/pengguna', methods=['GET','POST'])
@login_required
def list():
    data = enumerate(User.query.all(), start=1)
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, password=form.password.data, email=form.email.data, is_admin=form.is_admin.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Pengguna baru telah ditambahkan.')
        return redirect(url_for('users.list'))
    
    return render_template('users/users.html', data=data, form=form, title='Pengguna')

@users.route('/admin/pengguna/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.name = form.name.data
        user.password = form.password.data
        user.email = form.email.data
        user.is_admin = form.is_admin.data
        
        db.session.commit()
        flash('Data Pengguna telah diubah.')
        return redirect(url_for('users.list'))
    
    form.name.data = user.name
    form.email.data = user.email
    form.is_admin.data = user.is_admin
    return render_template('users/edit.html', form=form, user=user, title='Edit Pengguna')

@users.route('/admin/pengguna/<id>/hapus', methods=['GET', 'POST'])
@login_required
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Pengguna telah dihapus.')
    return redirect(url_for('users.list'))