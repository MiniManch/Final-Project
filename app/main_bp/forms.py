from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, FileField, SelectField, IntegerField, BooleanField)
from wtforms.validators import InputRequired, Length


class New_Guide(FlaskForm):
	subject            = StringField('Subject', validators=[InputRequired(),Length(min=10)], render_kw={"placeholder": 'for instance, How to change a Light Bulb'})
	description         = StringField('Description', validators=[InputRequired()])
	image               = FileField('Image')
	category = SelectField('Category')
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
	tools            = StringField('Tools')
	submit           = SubmitField('Submit')


class New_Item(FlaskForm):
	name                = StringField('name', validators=[InputRequired()], render_kw={"placeholder": 'Name'})
	description         = StringField('description', validators=[InputRequired()])
	image               = FileField('Image')
	price               = IntegerField('Price')
	guides              = StringField('Guide')
	fixed               = BooleanField('Has this item been fixed?')
	submit              = SubmitField('Submit')


class Search(FlaskForm):
	text = StringField('Search')
	submit           = SubmitField()


class Rating(FlaskForm):
	description         = StringField('description')
	rating               = IntegerField('')
	submit              = SubmitField('Submit')