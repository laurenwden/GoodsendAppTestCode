from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email

class UserInfoForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired()])
    last_name = StringField('Last Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password',validators =[DataRequired(),EqualTo('password')])
    submit = SubmitField()

class CaseForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    note = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField()