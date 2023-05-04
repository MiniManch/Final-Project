from flask import Blueprint
from app import db, flask_app
# from app.main_bp.models import Card
from app.getdata import populate_data
main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')

# with flask_app.app_context():
# 	populate_data()

from app.main_bp import routes
