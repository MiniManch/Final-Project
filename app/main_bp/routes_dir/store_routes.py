import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import New_Item
from app.accounts_bp.models import User
from app.utils import get_image, upload_image
import requests

@main_bp.route('/new_item', methods=['GET', 'POST'])
@login_required
def newitem():
	is_admin = current_user.username == 'admin'

	form = New_Item()
	if flask.request.method == 'POST':
		try:
			image = form.image.data
			if image.filename == '':
				image = 'business_gtx1hm'
			else:
				image = upload_image(image)

			item = models.Item(
				name=form.name.data,
				seller=current_user.id,
				description=form.description.data,
				image=image,
				guide=form.guide.data,
				fixed=form.fixed.data,
				price=form.price.data,
			)
			db.session.add(item)
			db.session.commit()
			flask.flash(f'New Item was created!')
			return flask.redirect(flask.url_for('main_bp.item', item_id=item.id))
		except Exception as e:
			print(e)
			flask.flash('Error has occurred')
			return flask.redirect(flask.url_for('main_bp.index'))
	return flask.render_template('/store/new_item.html', form=form, title="New Item")


@main_bp.route('/item/<int:item_id>', methods=['GET', 'POST'])
def item(item_id):
	try:
		this_item = models.Item.query.filter_by(id=item_id).first()
		return flask.render_template('/store/item.html', item=this_item, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Item you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))


@main_bp.route('/item/edit/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edititem(item_id):
	try:
		form = New_Item()

		this_item = models.Step.query.filter_by(id=item_id).first()

		is_author = this_item.seller == current_user.id
		is_admin = current_user.username == 'admin'

		if not is_admin or not is_author:
			flask.flash('You cannot change this Item.')
			return flask.redirect(flask.url_for('main_bp.index'))

		if flask.request.method == "POST":
			this_item.subject = form.name.data
			this_item.description = form.description.data
			this_item.image = upload_image(form.image.data)
			this_item.price = form.price.data
			this_item.fixed = form.fixed.data,
			this_item.guide = form.guide.data,
			db.session.commit()

			flask.flash('Item was changed successfully')
			return flask.redirect(flask.url_for('main_bp.item', item_id=this_item.id))

		form.name.data = this_item.name
		form.description.data = this_item.description
		form.price.data = this_item.price
		form.fixed.data = this_item.fixed
		form.guide.data = this_item.guide
		return flask.render_template('/store/new_item.html',edit = get_image(this_item.image), form=form, item=this_item, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Item you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))


@main_bp.route("/store/items")
def items():
	items_list = list(models.Item.query.filter_by(sold=False))
	return flask.render_template('/store/items.html', items=items_list, users=User, style='main/guides.css')


@main_bp.route("/store/my_items")
@login_required
def myitems():
	items_list = list(models.Item.query.filter_by(seller=current_user.id))
	return flask.render_template('/store/items.html', items=items_list, users=User, style='main/guides.css')
