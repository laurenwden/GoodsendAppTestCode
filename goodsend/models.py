from goodsend import app, db, login

#Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime

from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return Waitlist.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    waitlist = db.Column(db.Boolean, nullable=True, default=True)
    queue = db.Column(db.Boolean, nullable=True, default=False)
    approved = db.Column(db.Boolean, nullable=True, default=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(150), nullable=True) 
    password = db.Column(db.String(256), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,first_name, last_name, email,phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)
 

    
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

 



