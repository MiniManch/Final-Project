from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, DateField,EmailField, FileField)
from wtforms.validators import InputRequired, Email, Length, EqualTo
import email_validator


class New_Guide(FlaskForm):
	subject            = StringField('Subject', validators=[InputRequired(),Length(min=10)], render_kw={"placeholder": 'for instance, How to change a Light Bulb'})
	description         = StringField('Description', validators=[InputRequired()])
	image               = FileField('Image')
	submit           = SubmitField('Submit')


class New_Tool(FlaskForm):
	name            = StringField('Name', validators=[InputRequired()], render_kw={"placeholder": 'Hammer! Screwdriver! '})
	usage         = StringField('Main Usage', validators=[InputRequired()])
	image               = FileField('Image')
	submit           = SubmitField('Submit')


class New_Step(FlaskForm):
	subject            = StringField('Subject', validators=[InputRequired()], render_kw={"placeholder": 'Title of this step'})
	content         = StringField('Content', validators=[InputRequired()])
	image               = FileField('Image')
	submit           = SubmitField('Submit')


class Search(FlaskForm):
	text = StringField('Search', validators=[InputRequired()])
	submit           = SubmitField('<i class="fa fa-search"></i>')

