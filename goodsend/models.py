from goodsend import app, db, login

#Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime

from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(150), nullable=True, unique=True)   
    password = db.Column(db.String(256), nullable = False)


    def __init__(self,first_name, last_name,email,phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

class Waitlist(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(150), nullable=True, unique=True)   
    password = db.Column(db.String(256), nullable = False)


    def __init__(self,first_name, last_name,email,phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)

 

class Approved(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(150), nullable=True, unique=True)   
    password = db.Column(db.String(256), nullable = False)


    def __init__(self,first_name, last_name,email,phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)

