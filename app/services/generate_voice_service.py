from app.services.tts_service import generate_tts
from app.services.file_service import upload_to_gofile, delete_local_file, generate_filename
from app.services.redis_service import cache_voice

VOICE_PREFIX = "voice"
NOTIFICATION_SOUND_PATH = "static/noti_sound.mp3"

def generate_voice_amount(amount: str) -> str:
    path = generate_tts(amount)
    audio_url = upload_to_gofile(path)
    cache_voice(amount, audio_url)
    delete_local_file(path)
    return audio_url