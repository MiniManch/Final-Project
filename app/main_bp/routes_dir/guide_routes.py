import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide
from app.accounts_bp.models import User
from app.utils import  upload_image


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