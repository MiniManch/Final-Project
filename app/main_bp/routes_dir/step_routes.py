import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import  New_Step
from app.accounts_bp.models import User
from app.utils import get_image, upload_image
import requests


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


@main_bp.route('/edit/step/<int:step_id>', methods=['GET', 'POST'])
def editstep(step_id):
	try:
		form = New_Step()

		this_step = models.Step.query.filter_by(id=step_id).first()
		this_guide = models.Guide.query.filter_by(id=this_step.guide).first()

		is_author = this_guide.author == current_user.id
		is_admin = User.query.filter_by(id=current_user.id).first().username == 'admin'

		if not is_admin or is_author:
			flask.flash('You cannot change this step.')
			return flask.redirect(flask.url_for('main_bp.index'))

		if flask.request.method == "POST":
			this_step.subject = form.subject.data
			this_step.content = form.content.data
			this_step.image = upload_image(form.image.data)
			this_step.accepted = False
			db.session.commit()

			flask.flash('Step was changed successfully')
			return flask.redirect(flask.url_for('main_bp.step',step_id = this_step.id))

		form.subject.data = this_step.subject
		form.content.data = this_step.content
		return flask.render_template('/step/new_step.html',edit = get_image(this_step.image), form=form, step=this_step, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Step you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))