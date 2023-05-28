from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField, EmailField, FileField)
from wtforms.validators import InputRequired, Email, Length, EqualTo
import email_validator


class User_Form(FlaskForm):
	email            = EmailField('Email', validators=[InputRequired(), Email()], render_kw={"placeholder": 'Email@Email.com'})
	password         = PasswordField('Password', validators=[InputRequired(),Length(min=8),EqualTo('password_confirm',message='Passwords must match')])
	password_confirm = PasswordField('Password Confirm', validators=[InputRequired()])
	username         = StringField('Username', validators=[InputRequired()], render_kw={"placeholder": 'xXUniqueUserNameXx'})
	about         = StringField('About')
	submit           = SubmitField('Submit')


class Update_User(FlaskForm):
	email = EmailField('Email', validators=[InputRequired(), Email()], render_kw={"placeholder": 'Email@Email.com'})
	username = StringField('Username', validators=[InputRequired()], render_kw={"placeholder": 'xXUniqueUserNameXx'})
	image    = FileField('Profile Image')
	about         = StringField('About')
	submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])
    confirm  = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Change Password!')