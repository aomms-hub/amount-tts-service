import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("UPSTASH_REDIS_REST_URL")
CLOUDINARY_API_NAME = os.getenv("CLOUDINARY_API_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")