import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide, New_Tool , New_Step , Search
from app.accounts_bp.models import User
from app.utils import get_image, upload_image


@main_bp.route("/")
@main_bp.route("/homepage")
def index():
	return flask.render_template('index.html')


import app.main_bp.routes_dir.guide_routes
import app.main_bp.routes_dir.tool_routes
import app.main_bp.routes_dir.step_routes
import app.main_bp.routes_dir.admin_routes



# @main_bp.route('/new_comment/<int:post_id>', methods=['GET', 'POST'])
# @login_required
# def newcomment(post_id):
# 	form = Post_Form()
# 	if form.validate_on_submit():
# 		try:
# 			post = models.Post.query.filter_by(id=post_id).first()
# 			new = models.Comment( author=current_user.id,
# 				                  subject=form.subject.data,
# 				                  content=form.body.data,
# 				                  thread=post_id)
# 			post.comments.append(new)
# 			db.session.commit()
# 			flask.flash('New Comment was created successfully')
# 			return flask.redirect(flask.url_for('main_bp.post', post_id=post_id))
# 		except Exception as e:
# 			print(e)
# 			flask.flash('Error has occurred')
# 			return flask.redirect(flask.url_for('main_bp.post', post_id=post_id))
#
# 	return flask.render_template('newcomment.html', form=form, title="New Comment")
