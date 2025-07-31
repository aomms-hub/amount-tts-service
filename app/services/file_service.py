import requests
import os
from datetime import datetime

URL = "https://upload.gofile.io/uploadfile"

def upload_to_gofile(filepath):
    with open(filepath, "rb") as f:
        files = {"file": f}
        response = requests.post(URL, files=files)

    if response.status_code == 200:
        result = response.json()
        print(result)
        if result['status'] == 'ok':
            data = result['data']
            return data['downloadPage']
    print("Upload failed:", response.text)
    return None

def generate_filename(prefix: str, message: str) -> str:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{prefix}_{message}_{timestamp}.mp3"

def delete_local_file(filepath):
    try:
        os.remove(filepath)
        print(f"Deleted local file: {filepath}")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error deleting file {filepath}: {e}")