
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


def populate_categories(database,model):
	my_list = {
		'Apparel':'https://i.ibb.co/tB0WPbV/SS21-Magnus-Torsne-BTS-Apparel-1384-EXP-2026-06-01.jpg',
		'Appliance':'https://assets.bizclikmedia.net/1336/d675f976d7928ca21831e5521b269885:153e3573aee52b14472a523ce0e11a04/gettyimages-1301959047-0-jpg.webp',
		'Vehicles':'https://img.freepik.com/premium-vector/eight-means-transport_24908-76348.jpg',
		'Computers':'https://www.punchtechnology.co.uk/wp-content/uploads/2022/11/Be-Quiet-Pure-Base-500FX-Gaming-Chassis-Front-Angle-with-RGB-Lighting-Close-600x600.jpg',
		'Electronics':'https://img.freepik.com/premium-vector/gadgets-electronic-large-set_146957-836.jpg?w=2000',
		'Household':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKz3dSaAyhj--g9bVYI0iZ_lQcJXLwukZ-TA&usqp=CAU'
	}
	for key in my_list:
		new = model(name=key,image=upload_image(my_list[key]))
		database.session.add(new)
	database.session.commit()

def create_category_list(model):
	choice_list = ['-Category-']
	for category in model.query.all():
		choice_list.append(category.name)
	return choice_list