from flask import flash, redirect, render_template, url_for, request, session, current_app, app, send_from_directory
from flask_login import login_required, login_user, logout_user, current_user
from flask_ckeditor import upload_fail, upload_success
from . import profile
from ....models import Profile, Work, Slide
from .forms import ProfileForm, WorkForm, SlideForm
from .... import db
import os

@profile.route('/admin/profil', methods=['GET', 'POST'])
@login_required
def config():
    profile = Profile.query.first()
    works = Work.query.filter(Work.profile_id == profile.id).all()
    slides = Slide.query.filter(Slide.profile_id == profile.id).all()
    
    form = ProfileForm(obj=profile)
    form2 = WorkForm()
    form3 = SlideForm()
    if form.submit1.data and form.validate_on_submit():
        profile.site_title = form.site_title.data
        profile.site_desc = form.site_desc.data
        profile.profile_name = form.profile_name.data
        profile.profile_occupation = form.profile_occupation.data
        profile.profile_desc = form.profile_desc.data
        db.session.commit()
        flash('Konfigurasi telah disimpan.')
        return redirect(url_for('profile.config'))
    
    elif form2.submit2.data and form2.validate_on_submit():
        work = Work(profile_id=profile.id, name=form2.name.data, icon=form2.icon.data, desc=form2.desc.data)
        db.session.add(work)
        db.session.commit()
        flash('Pekerjaan telah ditambahkan.')
        return redirect(url_for('profile.config'))
        
    elif form3.submit3.data and form3.validate_on_submit():
        slide = Slide(profile_id=profile.id, name=form3.name.data)
        db.session.add(slide)
        db.session.commit()
        flash('Deskripsi telah ditambahkan.')
        return redirect(url_for('profile.config'))
        
    return render_template('config/list.html', profile=profile, works=works, slides=slides, form=form, form2=form2, form3=form3, title='Konfigurasi')

@profile.route('/admin/slide/<id>', methods=['GET', 'POST'])
@login_required
def del_slide(id):
    slide = Slide.query.get_or_404(id)
    db.session.delete(slide)
    db.session.commit()
    flash('Slide Teks telah dihapus.')
    return redirect(url_for('profile.config'))

@profile.route('/admin/work/<id>', methods=['GET', 'POST'])
@login_required
def del_work(id):
    work = Work.query.get_or_404(id)
    db.session.delete(work)
    db.session.commit()
    flash('Pekerjaan telah dihapus.')
    return redirect(url_for('profile.config'))
