import flask
from app.accounts_bp import accounts_bp, models
from app import db
from .forms import User_Form, Update_User
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import random
from app.utils import get_image, upload_image


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
                                   image = 'default_user_image.png'
                                   )
            db.session.add(new_user)
            db.session.commit()
            flask.flash(f'new user {form.username.data} is created!')
            return flask.redirect(flask.url_for('main_bp.index'))

        flask.flash('User already exists, try again')
        return flask.redirect(flask.url_for('accounts_bp.signup'))
    return flask.render_template("signup.html", form=form, title='Sign up')


@accounts_bp.route("/login", methods=['GET', 'POST'])
def login():
    form = User_Form()
    if flask.request.method == 'POST':
        user =  models.User.query.filter_by(email=form.email.data).first()
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
    return flask.render_template("login.html", form=form, title='Login')


@accounts_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('main_bp.index'))


@accounts_bp.route('/profile',methods=['GET', 'POST'])
@login_required
def profile():
    form = Update_User()
    if form.validate_on_submit():
        user_by_email = models.User.query.filter_by(email=form.email.data).first()
        user_by_username = models.User.query.filter_by(username=form.username.data).first()
        image = flask.request.files['image']
        if image.filename is not '':
            image = upload_image(image)
            current_user.image = image
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
    return flask.render_template('profile.html', form = form)



