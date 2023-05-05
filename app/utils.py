
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
	image_info = cloudinary.api.resource(image_id)
	return image_info

