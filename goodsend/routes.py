from goodsend import app#, db
from flask import render_template, request, redirect, url_for
# import forms
from goodsend.forms import UserInfoForm, CaseForm, LoginForm
#import models
#from goodsend.models import User, Case, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user

#Register Route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        email = form.email.data
        print("\n",username,password,email)
        # Create an instance of User
        user = User(username,email,password)
        # Open and insert into database
        db.session.add(user)
        # Save info into database
        db.session.commit()
    return render_template('register.html',form = form)

    #Login
@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html',form = form)