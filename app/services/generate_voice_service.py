from app.services.tts_service import generate_tts
from app.services.file_service import upload_to_cloudinary, delete_local_file
from app.services.redis_service import cache_voice

VOICE_PREFIX = "voice"
NOTIFICATION_SOUND_PATH = "static/noti_sound.mp3"

def generate_voice_amount(amount: str) -> str:
    path = generate_tts(amount)
    audio_url = upload_to_cloudinary(path, amount)
    cache_voice(amount, audio_url)
    delete_local_file(path)
    return audio_url