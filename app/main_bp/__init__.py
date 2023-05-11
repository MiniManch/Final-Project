from flask import Blueprint

main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/static/main')

from app.main_bp import routes
