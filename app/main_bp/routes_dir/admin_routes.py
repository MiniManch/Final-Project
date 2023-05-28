import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.accounts_bp.models import User


@main_bp.route("/guides_to_accept")
@login_required
def guides_to_accept():
	if current_user.username == 'admin':
		guides_list = list(models.Guide.query.filter_by(accepted=False))
		return flask.render_template('/guide/guides.html', guides=guides_list, users=User, accepting=True, style='main/guides.css')
	else:
		flask.flash('The page you are trying to view is restricted')
		return flask.redirect(flask.url_for('main_bp.index'))


@main_bp.route("/tools_to_accept")
@login_required
def tools_to_accept():
	if current_user.username == 'admin':
		tools_list = list(models.Tool.query.filter_by(accepted=False))
		return flask.render_template('/tools/tools.html', tools=tools_list, form=False, style='main/tools.css', accepting=True)
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
				return flask.redirect(flask.url_for('main_bp.index'))

			for index, step in enumerate(to_accept.steps):
				if not step.accepted:
					flask.flash(f'Step {index + 1} was not accepted please accept it to continue')
					# 			redirect to step page
					return flask.redirect(flask.url_for('main_bp.step', step_id=step.id))
			to_accept.accepted = True
			db.session.commit()
			flask.flash('Guide was accepted successfully!')
			return flask.redirect(flask.url_for('main_bp.guide', guide_id=to_accept.id))

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
			return flask.redirect(flask.url_for('main_bp.tools'))

	except Exception as e:
		print(e)
		flask.flash('an error has occurred')
		return flask.redirect(flask.url_for('main_bp.index'))
