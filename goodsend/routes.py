from goodsend import app, db, Message, mail
from flask import render_template, request, redirect, url_for
# import forms
from goodsend.forms import UserInfoForm, LoginForm
#import models
from goodsend.models import Waitlist, Onboarded, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user
import os
import stripe

stripe.api_key = os.environ.get('STRIPE_KEY')
#Home Route
@app.route('/data')
@login_required
def home():
    balance = stripe.Balance.retrieve()
    registered = Waitlist.query.all()
    active = Onboarded.query.all()
    active_count = 0
    count = 0
    users = 1
    current = current_user.id
    users_before = current - users
    for user in registered:
        count += 1
    for a in active:
        active_count += 1
    return render_template("data.html", balance = balance, count = count, users_before = users_before, active_count = active_count)

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
        waitlist = Waitlist(first_name,last_name,email, phone_number, password)
        # Open and insert into waitlist
        db.session.add(waitlist)
        # Save info into database
        db.session.commit()
        #Email service funnel for new users
        msg = Message(f'{email} has signed up!', recipients=[email])
        msg.body =('Another user has signed up')
        msg.html = ('<h1> Welcome to Goodsend! </h1>' '<p> Thank you for signing up! </p>')
        mail.send(msg)
    return render_template('register.html',form = form)

    #Login
@app.route('/', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = Waitlist.query.filter(Waitlist.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            print("logged in")
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html',form = form)

#Logout
@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('login'))

