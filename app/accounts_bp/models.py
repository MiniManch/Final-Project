from flask_login import UserMixin
from app import db
import time
import jwt


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
	items_on_sale = db.relationship('Item', backref='items')

	def get_reset_password_token(self, app, expires_in=600):
		timeout = time.time() + expires_in
		payload = {
			'reset_password': self.id,
			'exp': timeout
		}

		# Get the secret key from config
		secret_key = app.config['SECRET_KEY']

		# Create the token
		token = jwt.encode(payload, secret_key, algorithm="HS256")
		print(type(token))


		return token

	def verify_reset_password_token(self, token, app):
		try:
			id = jwt.decode(token, app.config['SECRET_KEY'],
			                algorithms=['HS256'])['reset_password']
		except:
			return
		return User.query.get(id)
