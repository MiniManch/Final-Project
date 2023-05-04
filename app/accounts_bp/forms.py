from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, DateField,EmailField)
from wtforms.validators import InputRequired, Email, Length, EqualTo
import email_validator


class User_Form(FlaskForm):
	email            = EmailField('Email', validators=[InputRequired(), Email()], render_kw={"placeholder": 'Email@Email.com'})
	password         = PasswordField('Password', validators=[InputRequired(),Length(min=8),EqualTo('password_confirm',message='Passwords must match')])
	password_confirm = PasswordField('Password Confirm', validators=[InputRequired()])
	username         = StringField('Username', validators=[InputRequired()], render_kw={"placeholder": 'xXUniqueUserNameXx'})
	submit           = SubmitField('Submit')

