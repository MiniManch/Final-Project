import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import Post_Form
from app.accounts_bp.models import User

@main_bp.route("/")
@main_bp.route("/homepage")
def index():
	return flask.render_template('index.html')

# FORUM AND POSTS
@main_bp.route("/forum")
@login_required
def forum():
	posts = models.Post.query.all()
	return flask.render_template('forum.html', posts=posts,users=User)


@main_bp.route('/new_post', methods=['GET', 'POST'])
@login_required
def newpost():
	form = Post_Form()
	if form.validate_on_submit():
		try:
			new = models.Post(author=current_user.id,
			                  subject=form.subject.data,
			                  content=form.body.data,
			                  comments=[])
			db.session.add(new)
			db.session.commit()
			flask.flash('New post was created successfully')
			return flask.redirect(flask.url_for('main_bp.forum'))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('newpost.html', form=form, title="New Post")


@main_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post(post_id):
	this_post = models.Post.query.filter_by(id=post_id).first()
	return flask.render_template('post.html', post=this_post, users=User)


@main_bp.route('/new_comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def newcomment(post_id):
	form = Post_Form()
	if form.validate_on_submit():
		try:
			post = models.Post.query.filter_by(id=post_id).first()
			new = models.Comment( author=current_user.id,
				                  subject=form.subject.data,
				                  content=form.body.data,
				                  thread=post_id)
			post.comments.append(new)
			db.session.commit()
			flask.flash('New Comment was created successfully')
			return flask.redirect(flask.url_for('main_bp.post', post_id=post_id))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.post', post_id=post_id))

	return flask.render_template('newcomment.html', form=form, title="New Comment")

#
# # TRANSACTIONS
# @main_bp.route('/new_transaction/<int:card_id>')
# @login_required
# def new_transaction(card_id):
# 	try:
# 		new = models.Transaction(author=current_user.id,
# 		                         offers=[],
# 		                         card=models.Card.query.filter_by(id=card_id).first().id)
# 		current_user.transactions.append(new)
# 		db.session.commit()
# 		flask.flash('New Transaction was created successfully')
# 		return flask.redirect(flask.url_for('main_bp.index'))
# 	except Exception as e:
# 		print(e)
# 		flask.flash('Error has occurred')
# 		return flask.redirect(flask.url_for('main_bp.index'))
#
#
# @main_bp.route('/transactions')
# @login_required
# def transactions():
# 	return flask.render_template('transactions.html', users=User, transactions=models.Transaction.query.all(), cards=models.Card)
