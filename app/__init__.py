import flask
import flask_mail
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from flask_login import LoginManager
import app.utils
from app.config import Config


flask_app = flask.Flask(__name__)
flask_app.config.from_object(Config)

mail = flask_mail.Mail(flask_app)

# configuring the database
db = SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

# Flask Login
login_manager = LoginManager()
login_manager.login_view = 'accounts_bp.login'
login_manager.init_app(flask_app)

from app.accounts_bp.models import User
from app.main_bp.models import Category,Tool

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))



# connection blueprints
from app.accounts_bp import accounts_bp
from app.main_bp import main_bp

flask_app.register_blueprint(accounts_bp, url_prefix="/accounts")
flask_app.register_blueprint(main_bp)

with flask_app.app_context():
	db.drop_all()
	db.create_all()
	# app.utils.populateDatabase(database=db, UserModel=User, ToolModel=Tool, CategoryModel=Category)
