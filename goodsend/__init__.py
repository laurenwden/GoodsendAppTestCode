from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
#Import for Flask Mail
from flask_mail import Mail, Message

#Import for flask login
from flask_login import LoginManager, current_user


app = Flask(__name__)
app.config.from_object(Config)
admin = Admin(app, template_mode="bootstrap3")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


login = LoginManager(app)
login.login_view = 'login' 

from goodsend import routes, models
from goodsend.models import Users


@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
        
        

admin.add_view(MyModelView(Users, db.session))







