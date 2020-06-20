from goodsend import app, db, Message, mail
from flask import render_template, request, redirect, url_for
# import forms
from goodsend.forms import UserInfoForm, LoginForm
#import models
from goodsend.models import User, Waitlist, Approved, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user
import os
import stripe
from config import Config

stripe.api_key = os.environ.get('STRIPE_KEY')
#Home Route
@app.route('/')
def home():
    balance = stripe.Balance.retrieve()
    return render_template("home.html", balance = balance)
#Register Route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        password = form.password.data
        print("\n", first_name, last_name, email,phone_number,password)
        # Create an instance of User
        user = User(first_name,last_name,email, phone_number, password)
        # Open and insert into database
        db.session.add(user)
        # Save info into database
        db.session.commit()
        msg = Message(f'{email} has signed up!', recipients=[email])
        msg.body =('Another user has signed up')
        msg.html = ('<h1> Welcome to Goodsend! </h1>' '<p> Thank you for signing up! </p>')
        mail.send(msg)
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
            print("logged in")
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html',form = form)

