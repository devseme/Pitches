import re
from flask import render_template,redirect,url_for,abort,flash,request

from app.main.forms import CategoryForm
from . import main
from flask_login import login_required,current_user

from app.models import Category, User,Post,Comment
from ..import db,photos
from .forms import CategoryForm
from slugify import slugify

@main.route('/')
def index():
    post = Post.query.order_by(Post.date_posted.desc()).all()
    print(post)
    return render_template('index.html')


@main.route('/add_category',methods=['GET','POST'])
# @login_required
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(Category)
        db.session.commit()
        flash[" You Succcessfully Added your Category!"]
        return redirect(url_for('.index'))
    return render_template('category.html',form=form)
