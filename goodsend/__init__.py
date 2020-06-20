from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView



#Import for flask login
from flask_login import LoginManager
# Create flask app variable
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)

login = LoginManager(app)
login.login_view = 'login' # Specify what page to load for NON-authenticated Users

from goodsend.models import User, Waitlist, Approved
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Waitlist, db.session))
admin.add_view(ModelView(Approved, db.session))

from goodsend import routes, models
