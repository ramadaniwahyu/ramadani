from flask import flash, redirect, render_template, url_for, request, session, app
from flask_login import login_required, login_user, logout_user, current_user
from . import categories
from ....models import Category
from .forms import CategoryForm
from .... import db

@categories.route('/admin/kategori', methods=['GET','POST'])
@login_required
def list():
    data = enumerate(Category.query.all(), start=1)
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data, url_name=form.url_name.data, desc=form.desc.data)
        db.session.add(category)
        db.session.commit()
        
        flash('Kategori baru telah ditambahkan.')
        return redirect(url_for('categories.list'))
    
    return render_template('categories/categories.html', data=data, form=form, title='Kategori')

@categories.route('/admin/kategori/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        category.desc = form.desc.data
        category.url_name = form.url_name.data
        
        db.session.commit()
        flash('Data kategori telah diubah.')
        return redirect(url_for('categories.list'))
    
    form.name.data = category.name
    form.desc.data = category.desc
    form.url_name.data = category.url_name
    return render_template('categories/edit.html', form=form, category=category, title='Edit Kategori')

@categories.route('/admin/kategori/<id>/hapus', methods=['GET', 'POST'])
@login_required
def delete(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Kategori telah dihapus.')
    return redirect(url_for('categories.list'))