import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide, New_Tool
from app.accounts_bp.models import User
from app.utils import get_image, upload_image


@main_bp.route("/")
@main_bp.route("/homepage")
def index():
	return flask.render_template('index.html')


# Guides
@main_bp.route("/guides")
def guides():
	guides_list = list(models.Guide.query.filter_by(accepted=True))
	return flask.render_template('guides.html', guides=guides_list, users=User, style='main/guide.css' )


@main_bp.route("/my_guides")
@login_required
def my_guides():
	guides_list = list(models.Guide.query.filter_by(author=current_user.id))
	return flask.render_template('guides.html', guides=guides_list, users=User, style='main/guide.css')


@main_bp.route('/new_guide', methods=['GET', 'POST'])
@login_required
def newguide():
	form = New_Guide()
	if flask.request.method == 'POST':
		try:
			image = form.image.data
			if image.filename == '':
				image = 'default_guide_cw0hsl'
			else:
				image = upload_image(image)

			guide = models.Guide(
				author=current_user.id,
				subject=form.subject.data,
				content=form.description.data,
				image=image,
				steps=[],
				accepted=False
			)
			db.session.add(guide)
			db.session.commit()
			flask.flash('New guide was created, please add some steps!')
			return flask.redirect(flask.url_for('main_bp.guide', guide_id=guide.id))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('new_guide.html', form=form, title="New Guide")


@main_bp.route('/guide/<int:guide_id>', methods=['GET', 'POST'])
def guide(guide_id):
	try:
		this_guide = models.Guide.query.filter_by(id=guide_id).first()
		current_author = this_guide.author == current_user.id
		is_admin = User.query.filter_by(id=current_user.id).first().username == 'admin'
		is_accepted = this_guide.accepted
		if current_author or is_admin or is_accepted:
			return flask.render_template('guide.html', guide=this_guide, users=User,style='main/guide.css')
			# return this_guide.author
	except Exception as e:
		print(e)
		flask.flash('the Guide you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))


# TOOLS
@main_bp.route('/new_guide', methods=['GET', 'POST'])
@login_required
def newtool():
	form = New_Tool()
	if flask.request.method == 'POST':
		try:
			image = form.image.data
			if image.filename == '':
				image = 'wrench_ctlq2a'
			else:
				image = upload_image(image)

			tool = models.Guide(
				author=current_user.id,
				name=form.name.data,
				usage=form.usage.data,
				image=image,
				accepted=False
			)
			db.session.add(tool)
			db.session.commit()
			flask.flash(f'New tool {tool.name} was created!')
			return flask.redirect(flask.url_for('main_bp.tool', tool_id=tool.id))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('new_tool.html', form=form, title="New Tool")



# Admin routes

@main_bp.route("/guides_to_accept")
@login_required
def guides_to_accept():
	if current_user.username == 'admin':
		guides_list = list(models.Guide.query.filter_by(accepted=False))
		return flask.render_template('guides.html', guides=guides_list, users=User, style='main/guide.css' )
	else:
		flask.flash('The page you are trying to view is restricted')
		return flask.redirect(flask.url_for('main_bp.index'))


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
