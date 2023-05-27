from werkzeug.security import generate_password_hash
import requests
# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv

load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)


def upload_image(image_file):
	result = cloudinary.uploader.upload(image_file)
	return result['public_id']


def get_image(image_id):
	image_info = f'https://res.cloudinary.com/drzcke4vu/image/upload/v1683294873/{image_id}'
	return image_info


def populate_categories(database, model):
	my_list = {
		'Apparel': 'https://i.ibb.co/tB0WPbV/SS21-Magnus-Torsne-BTS-Apparel-1384-EXP-2026-06-01.jpg',
		'Appliance': 'https://assets.bizclikmedia.net/1336/d675f976d7928ca21831e5521b269885:153e3573aee52b14472a523ce0e11a04/gettyimages-1301959047-0-jpg.webp',
		'Vehicles': 'https://img.freepik.com/premium-vector/eight-means-transport_24908-76348.jpg',
		'Computers': 'https://www.punchtechnology.co.uk/wp-content/uploads/2022/11/Be-Quiet-Pure-Base-500FX-Gaming-Chassis-Front-Angle-with-RGB-Lighting-Close-600x600.jpg',
		'Electronics': 'https://img.freepik.com/premium-vector/gadgets-electronic-large-set_146957-836.jpg?w=2000',
		'Household': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKz3dSaAyhj--g9bVYI0iZ_lQcJXLwukZ-TA&usqp=CAU'
	}
	for key in my_list:
		new = model(name=key, image=upload_image(my_list[key]))
		database.session.add(new)
	database.session.commit()


def create_category_list(model):
	choice_list = ['-Category-']
	for category in model.query.all():
		choice_list.append(category.name)
	return choice_list


def populate_admin_user(database, model):
	new = model(email='admin@admin.com',
	            password=generate_password_hash('12345678', method='sha256'),
	            username='admin',
	            image='default_user_image.png')
	database.session.add(new)
	database.session.commit()
	return new


def populate_tools(database, model, author):
	my_list = [
		{'name': 'Tape Measure',
		 'image': 'https://images.thdstatic.com/productImages/ec09565d-3822-4271-bc81-26600126588a/svn/stanley-tape-measures-33-425d-64_1000.jpg',
		 'usage': 'length measurement'},

		{'name': 'Utility Knife',
		 'image': 'https://www.callcarton.co.il/wp-content/uploads/2020/12/%D7%A1%D7%9B%D7%99%D7%9F-%D7%99%D7%A4%D7%A0%D7%99%D7%AA.jpg',
		 'usage': 'Make percision cuts'},

		{'name': 'Pliers',
		 'image': 'https://cdn.britannica.com/00/125400-004-308C8DD9/Needle-nose-pliers.jpg',
		 'usage': 'Hold objects firmly'},

		{'name': 'Hammer',
		 'image': 'https://www.sccssurvey.co.uk/media/catalog/product/cache/2412bf1066845f9fbbd3b1fa4251e6b8/c/l/claw_hammer.jpg',
		 'usage': 'Usually to nail nails or deliver a strong impact to an object'},

		{'name': 'Level',
		 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9W9R2QAqYDg8rMIHzFs-u0dL9S1ly94SA-QnkVfarv4xsotOkuGSJxGhOo2LPEPGrWew&usqp=CAU',
		 'usage': 'Designed to indicate wether a surface is horizontal or vertical.'},

		{'name': 'Screwdriver',
		 'image': 'https://www.knipex-tools.com/sites/default/files/styles/knipex_product_detail/public/982402-00-3.jpg?itok=A12PVlDh',
		 'usage': 'Used for turning screws.'},

		{'name': 'Drill',
		 'image': 'https://cdn.hswstatic.com/gif/power-drill-1.jpg',
		 'usage': 'For making round holes or driving fasteners.'},

		{'name': 'Clamp',
		 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxZt4NA10On50dUI3F2R5sL9XikcfMdgl0-g&usqp=CAU',
		 'usage': 'Fastening device used to hold or secure objects tightly'},

		{'name': 'Flashlight',
		 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBYRDzHSNY2ncdljh0lfbETejF19HAMuZmCQ&usqp=CAU',
		 'usage': 'Provide light source.'},

		{'name': 'Opening Tool',
		 'image': 'https://cdn.shopify.com/s/files/1/0045/4092/4007/products/dPx63wucK43PlWnH.jpg?v=1667237862&width=1080',
		 'usage': 'The primary tool for opening everything.'},

		{'name': 'PlayStation 4 Battery',
		 'image': 'https://cdn.shopify.com/s/files/1/0045/4092/4007/products/x5sZ6YXXx1yxCcid_73d67002-7c99-4313-9f6c-341f40d839af.jpg?v=1667246896&width=1080',
		 'usage': 'This PlayStation 4 Controller (JDM-040) Battery'},

		{'name': 'Tweezers',
		 'image': 'https://cdn.shopify.com/s/files/1/0045/4092/4007/products/SgcjxIZnNVleJooT.jpg?v=1667237329&width=1080',
		 'usage': 'Grab hold of your repairs with authority.'},

	]
	for item in my_list:
		new = model(name=item['name'],
		            image=upload_image(item['image']),
		            usage=item['usage'],
		            author=author.id,
		            accepted=True)
		database.session.add(new)
	database.session.commit()

def populateDatabase(database, UserModel, ToolModel, CategoryModel):
	populate_categories(database=database, model=CategoryModel)
	populate_tools(database=database, model=ToolModel, author=populate_admin_user(database=database, model=UserModel))




