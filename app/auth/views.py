from flask import render_template,redirect,url_for,flash,request
from flask_login.utils import login_required, logout_user
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm
from .. import db


#registering user route
@auth.route("/redister",methods=["GET","POST"])
def register():
    forms = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.date,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Your registration was successful.Login now...")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=form,title='Register')   

    #login user route
     