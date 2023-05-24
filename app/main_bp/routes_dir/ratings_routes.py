import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import Rating
from app.accounts_bp.models import User
from app.utils import  upload_image, get_image , create_category_list


@main_bp.route("/rate/<int:guide_id>/<int:num_of_stars>",methods=['GET','POST'])
@login_required
def rate(guide_id,num_of_stars):
	try:
		guide = models.Guide.query.filter_by(id=guide_id).first()
		author = User.query.filter_by(id=guide.author).first()
		if current_user.id == guide.author:
			flask.flash('You cant review your own guide :)')
			return flask.redirect(flask.url_for('main_bp.index'))

		for review in guide.reviews:
			if review.author == current_user.id:
				flask.flash('You have already reviewed this guide!')
				return flask.redirect(flask.url_for('main_bp.index'))
		rating = num_of_stars
		form  = Rating()
		if flask.request.method == 'POST':
			if form.rating.data is None:
				flask.flash('You have to choose atleast 1 stars :)')
				return flask.redirect(flask.url_for('main_bp.index'))
			new_rate = models.Rating(
				author=current_user.id,
				content=form.description.data,
				rate=form.rating.data,
				guide=guide.id,
			)
			guide.num_of_ratings = guide.num_of_ratings + 1
			guide.rating = guide.rating + form.rating.data/guide.num_of_ratings
			guide.reviews.append(new_rate)


			db.session.add(new_rate)
			db.session.commit()
			flask.flash('Thank you for your review!')
			return flask.redirect(flask.url_for('main_bp.index'))
	except Exception as e:
		print(e)
		flask.flash('Error has occurred')
		return flask.redirect(flask.url_for('main_bp.index'))

	return flask.render_template('/rating/rate.html',title=f'You are rating: \n {guide.subject}', form = form, style='main/new.css')

