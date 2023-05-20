import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Guide,Search
from app.accounts_bp.models import User
from app.utils import  upload_image, get_image , create_category_list


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
			category = models.Category.query.filter_by(name = form.category.data).first()

			guide = models.Guide(
				author=current_user.id,
				subject=form.subject.data,
				content=form.description.data,
				rating=0,
				num_of_ratings=0,
				image=image,
				category = category.id,
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
	form.category.choices = create_category_list(models.Category)
	return flask.render_template('/guide/new_guide.html', form=form, style='main/new.css', title="New Guide")


@main_bp.route('/guide/<int:guide_id>', methods=['GET', 'POST'])
def guide(guide_id):
	try:
		this_guide = models.Guide.query.filter_by(id=guide_id).first()
		is_author = False
		is_admin = False
		if current_user.is_authenticated:
			is_author = this_guide.author == current_user.id
			is_admin = current_user.username == 'admin'
		is_accepted = this_guide.accepted
		if is_author or is_admin or is_accepted:
			return flask.render_template('/guide/guide.html', guide=this_guide, users=User, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Guide you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))


@main_bp.route('/guide/edit/<int:guide_id>', methods=['GET', 'POST'])
@login_required
def editguide(guide_id):
	try:
		form = New_Guide()
		this_guide = models.Guide.query.filter_by(id=guide_id).first()

		is_author = this_guide.author == current_user.id
		is_admin = current_user.username == 'admin'

		if not is_admin or not is_author:
			flask.flash('You cannot change this guide.')
			return flask.redirect(flask.url_for('main_bp.index'))

		if flask.request.method == "POST":
			this_guide.subject = form.subject.data
			this_guide.content = form.description.data
			this_guide.image = upload_image(form.image.data)
			this_guide.accepted = False
			db.session.commit()

			flask.flash('Guide was changed successfully')
			return flask.redirect(flask.url_for('main_bp.guide', guide_id= this_guide.id))

		form.subject.data = this_guide.subject
		form.description.data = this_guide.content
		form.category.choices = create_category_list(models.Category)
		form.category.data  = models.Category.query.filter_by(id=this_guide.category).first().name
		return flask.render_template('/guide/new_guide.html', edit=get_image(this_guide.image), title='Edit Guide', form=form, guide=this_guide, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Guide you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))