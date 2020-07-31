from goodsend import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from flask_admin import Admin, expose
from goodsend.forms import UserInfoForm, LoginForm
from goodsend.models import Users, check_password_hash
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required,login_user,current_user,logout_user
import os
# import stripe

# stripe.api_key = os.environ.get('STRIPE_KEY')
admin_username = os.environ.get('ADMIN_USERNAME')
admin_password = os.environ.get('ADMIN_PASSWORD')


#Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#Home Route
@app.route('/portalhome')
@login_required
def home():
    if current_user.waitlist == True:
        return redirect(url_for('waitlist'))
    elif current_user.approved == True:
        return redirect(url_for('login'))
    return redirect(url_for('login'))
    
    
    # balance = stripe.Balance.retrieve()
    # amount_total = balance["available"][0]["amount"]
    # approved_count = 0
    # for approved in approved_beneficiaries:
    #     approved_count += 1
    # if approved_count <= 0:
    #     dollar_amount = 0
    # else:
    #     dollar_amount = amount_total / approved_count
    # active = Users.query.all()
    # active_count = 0
    # count = 0
    # users = 1
    # current = current_user.id
    # users_before = current - users - 1
    # status = Users.query.filter_by(id = current_user.id).first()

    
    # is_wait = status.waitlist
    # is_queue = status.queue
    # is_approved = Users.query.filter_by(id = current_user.id).first().approved
    # for a in active:
    #     active_count += 1
    # for i in waitlst:
    #     count += 1
    # return render_template("portalhome.html", balance=balance, count=count, users_before=users_before, active_count=active_count, is_wait = is_wait, is_queue = is_queue, is_approved = is_approved, dollar_amount=dollar_amount)



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
        user = Users(first_name,last_name,email, phone_number, password)
        # Open and insert into waitlist
        db.session.add(user)
        # Save info into database
        db.session.commit()
        #Email service funnel for new users and 2nd string is admin email
        #msg = Message(f'{email} has signed up!', recipients=[email, 'goodsendtest1@gmail.com'])
        #msg.body =('Another user has signed up')
        #msg.html = ('<h1> Welcome to Goodsend! </h1>' '<p> Thank you for signing up! </p>')
        #mail.send(msg)
        print("registered")
    return render_template('register.html',form = form)

#Login
@app.route('/', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        if form.email.data == "admintest123@123.com" and form.password.data == "password123":
            logged_user = Users.query.filter(Users.email == email).first()
            login_user(logged_user)
            print('Logged in!')
            return redirect(url_for('admin.index'))
        else:
            logged_user = Users.query.filter(Users.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                print("logged in")
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    return render_template('login.html', form=form)
    
@app.route('/portal1')
@login_required
def waitlist():
    # balance = stripe.Balance.retrieve()
    # amount_total = balance["available"][0]["amount"]
    active = Users.query.all()
    active_count = 0
    count = 0
    users = 1
    current = current_user.id
    users_before = current - users - 1
    status = Users.query.filter_by(id = current_user.id).first()
    waitlst = Users.query.filter_by(waitlist = True).all()
    is_wait = status.waitlist
    for a in active:
        active_count += 1
    for i in waitlst:
        count += 1
    return render_template("portal1.html", count=count, users_before=users_before, active_count=active_count, is_wait=is_wait)
    

