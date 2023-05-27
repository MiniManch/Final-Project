import flask
from app.accounts_bp import accounts_bp, models
from app import db, mail,flask_app
import flask_mail
import os
import jwt
from .forms import User_Form, Update_User, ResetPasswordRequestForm,ResetPasswordForm
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils import get_image, upload_image


def send_email(subject, sender, recipients, html_body):
    msg = flask_mail.Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token(flask_app)
    send_email('Password reset',
               sender=os.environ['MAIL_APP_USERNAME'],
               recipients=[user.email],
               html_body=flask.render_template('email/reset_password.html', user=user, token=token))


@accounts_bp.route("/signup", methods=['GET', 'POST'])
def signup():
	form = User_Form()
	if form.validate_on_submit():
		email = models.User.query.filter_by(email=form.email.data).first()
		username = models.User.query.filter_by(username=form.username.data).first()
		if email is None and username is None:
			new_user = models.User(email=form.email.data,
			                       password=generate_password_hash(form.password.data, method='sha256'),
			                       username=form.username.data,
			                       about=form.about.data,
			                       image='default_user_image.png'
			                       )
			db.session.add(new_user)
			db.session.commit()
			flask.flash(f'new user {form.username.data} is created!')
			return flask.redirect(flask.url_for('main_bp.index'))

		flask.flash('User already exists, try again')
		return flask.redirect(flask.url_for('accounts_bp.signup'))
	return flask.render_template("signup.html", form=form, title='Sign up', style='accounts/new.css')


@accounts_bp.route("/login", methods=['GET', 'POST'])
def login():
	form = User_Form()
	if flask.request.method == 'POST':
		user = models.User.query.filter_by(email=form.email.data).first()
		if user is None:
			flask.flash('Email does not exist , try again')
			return flask.redirect(flask.url_for('accounts_bp.login'))
		else:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				flask.flash(f'Welcome {current_user.username}')
				return flask.redirect(flask.url_for('main_bp.index'))

			else:
				flask.flash('Wrong password, try again')
				return flask.redirect(flask.url_for('accounts_bp.login'))
	return flask.render_template("login.html", form=form, title='Login', style='accounts/new.css')


@accounts_bp.route('/logout')
@login_required
def logout():
	logout_user()
	return flask.redirect(flask.url_for('main_bp.index'))


@accounts_bp.route('/profile')
@login_required
def profile():
	return flask.render_template('profile.html', user=current_user, style='accounts/user.css')


@accounts_bp.route('/view/profile/<int:user_id>')
def view_profile(user_id):
	user = models.User.query.filter_by(id=user_id).first()
	if user is None:
		flask.flash('Cannot find this user try again')
		return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('profile.html', user=user, style='accounts/user.css')


@accounts_bp.route('edit/profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_profile(user_id):
	if user_id is not current_user.id:
		flask.flash('You cannot access this page')
		return flask.redirect(flask.url_for('main_bp.index'))

	form = Update_User()
	if form.validate_on_submit():
		user_by_email = models.User.query.filter_by(email=form.email.data).first()
		user_by_username = models.User.query.filter_by(username=form.username.data).first()
		image = flask.request.files['image']
		if image.filename != 'Your  Picture.jpg':
			image = upload_image(image)
			current_user.image = image
		current_user.about = form.about.data
		checker = 0
		if user_by_email is None or user_by_email.email == current_user.email:
			current_user.email = form.email.data
			checker = 1
		if user_by_username is None or user_by_username.username == current_user.username:
			current_user.username = form.username.data
			checker = 1
		if checker == 1:
			db.session.commit()
			flask.flash('Details were changed successfully')
			return flask.redirect(flask.url_for('accounts_bp.profile'))
		flask.flash('Cant update those details, they already exist, try again')
		return flask.redirect(flask.url_for('accounts_bp.profile'))
	return flask.render_template('edit_profile.html', form=form, style='accounts/new.css', title='Edit Profile',
	                             edit=get_image(current_user.image), )


@accounts_bp.route('change_password/<int:user_id>', methods=['GET', 'POST'])
def change_password(user_id):
	user=models.User.query.filter_by(id=user_id).first()
	if user is None:
		flask.flash('An error has occurred')
		return flask.redirect(flask.url_for('main_bp.index'))

	form = ResetPasswordForm()
	if form.validate_on_submit():
		user.password = generate_password_hash(form.password.data, method='sha256')
		db.session.commit()
		flask.flash('Details were changed successfully')
		return flask.redirect(flask.url_for('accounts_bp.login'))

	return flask.render_template('change_password.html',form=form,title='Change Passowrd', style='accounts/new.css')


@accounts_bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():

    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('main_bp.index'))

    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()

        if user:
            send_password_reset_email(user)

        flask.flash('An email has been sent')
        return flask.redirect(flask.url_for('accounts_bp.login'))
    return flask.render_template('reset_password_request.html', style='accounts/new.css', title='Reset Password', form=form)




