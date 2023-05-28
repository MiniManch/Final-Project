from flask import Blueprint

accounts_bp = Blueprint('accounts_bp', __name__, template_folder='templates', static_folder='static')

from app.accounts_bp import routes