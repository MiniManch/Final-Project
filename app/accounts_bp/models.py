from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	username = db.Column(db.String(100), unique=True)
	guides   = db.relationship('Guide', backref='guide-creator')
	reputation = db.Column(db.Float)
	ratings   = db.relationship('Rating', backref='rater')
	image    = db.Column(db.String(100))
	tools   = db.relationship('Tool', backref='tool-creator')


# from app.main_bp.models import Card

# after image is uploaded to cloudinary, we want to save the public id of it
