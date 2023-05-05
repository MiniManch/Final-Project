import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide
from app.accounts_bp.models import User
@main_bp.route("/")
@main_bp.route("/homepage")
def index():
	return flask.render_template('index.html')

# FORUM AND POSTS
@main_bp.route("/guides")
def guides():
	guides_list = models.Guide.query.all()
	return flask.render_template('guides.html', guides=guides_list, users=User)


@main_bp.route('/new_guide', methods=['GET', 'POST'])
@login_required
def newguide():
	form = New_Guide()
	if form.validate_on_submit():
		try:
			pass
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('new_guide.html', form=form, title="New Guide")

#
# @main_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
# @login_required
# def post(post_id):
# 	this_post = models.Post.query.filter_by(id=post_id).first()
# 	return flask.render_template('post.html', post=this_post, users=User)
#
#
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
