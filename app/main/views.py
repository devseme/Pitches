import re
from flask import render_template,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user

from app.models import User,Post,Comment

@main.route('/')
def index():
    post = Post.query.order_by(Post.posting_date.desc()).all()
    print(post)
    return render_template('index.html')