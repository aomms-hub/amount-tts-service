import cloudinary
import cloudinary.uploader
import os
from config import CLOUDINARY_API_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

cloudinary.config(
    cloud_name=CLOUDINARY_API_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True
)


def upload_to_cloudinary(filepath, amount: str):
    try:
        response = cloudinary.uploader.upload(
            filepath,
            resource_type="auto",  # หรือ "auto" ก็ได้ สำหรับ mp3
            public_id=generate_filename("tts", amount),
            overwrite=True,
            folder="pay_alert_audio"
        )
        url = response.get("secure_url")
        return url
    except Exception as e:
        print("Upload failed:", e)
        return None


def generate_filename(prefix: str, amount: str) -> str:
    return f"{prefix}_{amount.replace('.', '')}_baht"


def delete_local_file(filepath):
    try:
        os.remove(filepath)
        print(f"Deleted local file: {filepath}")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error deleting file {filepath}: {e}")
