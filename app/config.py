import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ['SECRET_KEY']
	UPLOAD_FOLDER = 'static/uploaded_images'
	# SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.environ["MYSQL_USER"]}:{os.environ["MYSQL_PASSWORD"]}@{os.environ["MYSQL_DATABASE"]}?charset=utf8mb4'
	SQLALCHEMY_DATABASE_URI = 'postgresql://finalproject_u06w_user:M0G4svlSPLokrdSWFFxfCwy6FK8SI0e1@dpg-chnp1482qv207f235afg-a.frankfurt-postgres.render.com/finalproject_u06w'

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_USERNAME = os.environ['MAIL_APP_USERNAME']
	MAIL_PASSWORD = os.environ['MAIL_APP_PASSWORD']

