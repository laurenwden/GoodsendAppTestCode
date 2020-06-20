from goodsend import app, db
from flask import render_template, request, redirect, url_for
# import forms
from goodsend.forms import UserInfoForm, CaseForm, LoginForm
#import models
from goodsend.models import User, Case, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user