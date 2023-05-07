from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, DateField,EmailField, FileField)
from wtforms.validators import InputRequired, Email, Length, EqualTo
import email_validator


class New_Guide(FlaskForm):
	subject            = StringField('Subject', validators=[InputRequired(),Length(min=10)], render_kw={"placeholder": 'for instance, How to change a Light Bulb'})
	description         = StringField('Description', validators=[InputRequired()])
	image               = FileField('Image')
	submit           = SubmitField('Submit')

