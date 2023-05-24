import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide, New_Tool , New_Step , Search
from app.accounts_bp.models import User
from app.utils import get_image, upload_image


@main_bp.route("/")
def index():
	guides = list(models.Guide.query.filter_by(accepted=True))[0:6];
	return flask.render_template('index.html', guides=guides, categories=models.Category, users=User)


import app.main_bp.routes_dir.guide_routes
import app.main_bp.routes_dir.tool_routes
import app.main_bp.routes_dir.step_routes
import app.main_bp.routes_dir.admin_routes
import app.main_bp.routes_dir.ratings_routes