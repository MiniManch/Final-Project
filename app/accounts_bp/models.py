from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	username = db.Column(db.String(100), unique=True)
	guides   = db.relationship('Guide', backref='author')
	image    = db.Column(db.String(200))

# from app.main_bp.models import Card


