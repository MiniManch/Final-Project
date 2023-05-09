import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide, New_Tool , New_Step
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
	return flask.render_template('/guide/guides.html', guides=guides_list, users=User, style='main/guides.css')


@main_bp.route("/my_guides")
@login_required
def my_guides():
	guides_list = list(models.Guide.query.filter_by(author=current_user.id))
	return flask.render_template('/guide/guides.html', guides=guides_list, users=User, style='main/guides.css')


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
	return flask.render_template('/guide/new_guide.html', form=form, title="New Guide")


@main_bp.route('/guide/<int:guide_id>', methods=['GET', 'POST'])
def guide(guide_id):
	try:
		this_guide = models.Guide.query.filter_by(id=guide_id).first()
		is_author = this_guide.author == current_user.id
		is_admin = current_user.username == 'admin'
		is_accepted = this_guide.accepted
		if is_author or is_admin or is_accepted:
			return flask.render_template('/guide/guide.html', guide=this_guide, users=User, style='main/guide.css')
		# return this_guide.author
	except Exception as e:
		print(e)
		flask.flash('the Guide you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))


# TOOLS
@main_bp.route('/new_tool', methods=['GET', 'POST'])
@login_required
def newtool():
	form = New_Tool()
	is_admin = current_user.username == 'admin'
	if flask.request.method == 'POST':
		try:
			image = form.image.data
			if image.filename == '':
				image = 'wrench_ctlq2a'
			else:
				image = upload_image(image)

			tool = models.Tool(
				author=current_user.id,
				name=form.name.data,
				usage=form.usage.data,
				image=image,
				accepted=is_admin
			)
			db.session.add(tool)
			db.session.commit()
			flask.flash(f'New tool {tool.name} was created!')
			return flask.redirect(flask.url_for('main_bp.tools'))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('/tools/new_tool.html', form=form, title="New Tool")


@main_bp.route("/tools")
def tools():
	tools_list = list(models.Tool.query.filter_by(accepted=True))
	return flask.render_template('/tools/tools.html', tools=tools_list, style='main/guides.css')


# STEPS
@main_bp.route('/new_step/<int:guide_id>', methods=['GET', 'POST'])
@login_required
def newstep(guide_id):
	is_admin = current_user.username == 'admin'
	guide = models.Guide.query.filter_by(id=guide_id).first()
	if current_user.id != guide.author or is_admin:
		flask.flash('You cannot change this guide.')
		return flask.redirect(flask.url_for('main_bp.index'))

	form = New_Step()
	if flask.request.method == 'POST':
		try:
			image = form.image.data
			if image.filename == '':
				image = 'going-to-fix-all-the-problems-in-your-house_qqynm2.jpg'
			else:
				image = upload_image(image)

			step = models.Step(
				subject=form.subject.data,
				content=form.content.data,
				image=image,
				guide=guide.id,
				accepted=is_admin

			)
			db.session.add(step)
			db.session.commit()
			flask.flash(f'New Step was created!')
			return flask.redirect(flask.url_for('main_bp.newstep', guide_id=guide.id))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('/step/new_step.html', form=form, title="New Step")


@main_bp.route('/step/<int:step_id>', methods=['GET', 'POST'])
def step(step_id):
	try:
		this_step = models.Step.query.filter_by(id=step_id).first()
		this_guide = models.Guide.query.filter_by(id=this_step.guide).first()

		is_author = this_guide.author == current_user.id
		is_admin = User.query.filter_by(id=current_user.id).first().username == 'admin'
		is_accepted = this_guide.accepted and this_step.accepted
		if is_accepted or is_author or is_admin :
			return flask.render_template('/step/step.html', guide=this_guide, step=this_step, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Step you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))


# Admin routes
@main_bp.route("/guides_to_accept")
@login_required
def guides_to_accept():
	if current_user.username == 'admin':
		guides_list = list(models.Guide.query.filter_by(accepted=False))
		return flask.render_template('/guide/guides.html', guides=guides_list, users=User, accepting=True, style='main/guides.css')
	else:
		flask.flash('The page you are trying to view is restricted')
		return flask.redirect(flask.url_for('main_bp.index'))


@main_bp.route("/accept/<what>/<int:its_id>")
@login_required
def accept(what, its_id):
	if current_user.username != 'admin':
		print(current_user.username)
		flask.flash('The page you are trying to view is restricted')
		return flask.redirect(flask.url_for('main_bp.index'))
	try:
		# guide accept.
		if what == 'guide':
			to_accept = models.Guide.query.filter_by(id=its_id).first()
			# 	check if its steps are accepted
			if len(to_accept.steps) == 0:
				flask.flash(f'This guide has no steps')
				return flask.redirect(flask.url_for('main_b.index'))

			for index, step in enumerate(to_accept.steps):
				if not step.accepted:
					flask.flash(f'Step {index + 1} was not accepted please accept it to continue')
					# 			redirect to step page
					return flask.redirect(flask.url_for('main_bp.step', step_id=step.id))
			to_accept.accepted = True
			db.session.commit()
			flask.flash('Guide was accepted successfully!')
			return flask.redirect(flask.url_for('main_bp.guide',guide_id=to_accept.id))

		# Step accept.
		if what == 'step':
			to_accept = models.Step.query.filter_by(id=its_id).first()
			to_accept.accepted = True
			db.session.commit()
			flask.flash('Step was accepted successfully!')
			return flask.redirect(flask.url_for('main_bp.step', step_id=to_accept.id))

		# Tool accept.
		if what == 'tool':
			to_accept = models.Tool.query.filter_by(id=its_id).first()
			to_accept.accepted = True
			db.session.commit()
			flask.flash('Tool was accepted successfully!')
			return flask.redirect(flask.url_for('main_bp.tool', step_id=to_accept.id))

	except Exception as e:
		print(e)
		flask.flash('an error has occurred')
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
