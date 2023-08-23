from flask import flash, redirect, render_template, url_for, abort
from . import frontend
from ...models import Page, Comment, Category, Profile, Contact
from .forms import CommentForm, ContactForm
from ... import db

@frontend.route('/beranda', methods=['GET','POST'])
def main_home():
    profile = Profile.query.first()
    posts = Page.query.all()
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, email=form.email.data, content=form.content.data)
        db.session.add(contact)
        db.session.commit()
        flash('Message has been sent.')
        return redirect(url_for('frontend.main_home'))
    
    return render_template('public/home.html', profile=profile, form=form, posts=posts, title='Beranda')

@frontend.route('/blog', methods=['GET','POST'])
def post():
    
    list = Page.query.all()
    types = Category.query.all()
    
    return render_template('public/blog.html', list=list, types=types, title='Blog')

@frontend.route('/blog/<id>', methods=['GET', 'POST'])
def post_item(id):
    post = Page.query.get_or_404(id)
    types = Category.query.all()
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(name=form.name.data, email=form.email.data, content=form.content.data, page_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Komentar telah ditambahkan')
        return redirect(url_for('frontend.post_item', id=post.id))
    
    return render_template('public/blog-inner.html', types=types, post=post, form=form, title='Blog -'+post.title)

@frontend.route('/kategori/<text>', methods=['GET','POST'])
def postByCategory(text):
    # txt = text.replace('-', ' ').capitalize()
    category = Category.query.filter_by(url_name=text).first()
    if not category: 
        abort(404)
    
    list = Page.query.filter_by(category_id = category.id).all()
   
    return render_template('public/post.html', list=list, title='Blog '+category.name)