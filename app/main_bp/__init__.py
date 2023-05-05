from flask import Blueprint
from app import db, flask_app
# from app.main_bp.models import Card
from app.utils import upload_image,get_image
main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')

# with flask_app.app_context():
# 	populate_data()

from app.main_bp import routes
