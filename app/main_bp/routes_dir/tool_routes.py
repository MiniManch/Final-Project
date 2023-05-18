import flask
from app.main_bp import main_bp
from flask_login import current_user, login_required
from app import db
import app.main_bp.models as models
from app.main_bp.forms import  New_Tool, Search
from app.utils import upload_image, get_image


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


@main_bp.route("/tools",methods=['GET','POST'])
def tools():
	form = Search()
	tools_list = list(models.Tool.query.filter_by(accepted=True))
	if flask.request.method == 'POST':
		try:
			searched_for = models.Tool.query.filter_by(name=form.text.data).first()
			if searched_for is None:
				flask.flash('Could not find what you were looking for, Sorry!')
				return flask.redirect(flask.url_for('main_bp.tools'))

			tools_list = [searched_for]
		except Exception as e:
			print(e)
			flask.flash('Could not find what you were looking for, Sorry!')
			return flask.redirect(flask.url_for('main_bp.tools'))
	return flask.render_template('/tools/tools.html', tools=tools_list, style='main/tools.css', form=form)


@main_bp.route('/tools/edit/<int:tool_id>', methods=['GET', 'POST'])
@login_required
def edittool(tool_id):
	try:
		form = New_Tool()
		this_tool = models.Tool.query.filter_by(id=tool_id).first()

		if flask.request.method == "POST":
			this_tool.name = form.name.data
			this_tool.usage = form.usage.data
			this_tool.image = upload_image(form.image.data)
			this_tool.accepted = False
			db.session.commit()

			flask.flash('Tool was changed successfully')
			return flask.redirect(flask.url_for('main_bp.tools', tool_id=this_tool.id))

		form.name.data = this_tool.name
		form.usage.data = this_tool.usage
		return flask.render_template('/tools/new_tool.html', edit=get_image(this_tool.image), form=form, tool=this_tool, style='main/guide.css')
	except Exception as e:
		print(e)
		flask.flash('the Tool you are trying to reach is unavailable at this moment')
		return flask.redirect(flask.url_for('main_bp.index'))