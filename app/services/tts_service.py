from gtts import gTTS
from app.services.file_service import generate_filename
import os

TTS_PREFIX = "tts"


def generate_tts(amount: str, lang: str = "th") -> str:
    filename = generate_filename(TTS_PREFIX, amount)
    tts = gTTS(text=generate_message(amount), lang=lang)
    output_path = os.path.join("static", filename)
    os.makedirs("static", exist_ok=True)
    tts.save(output_path)
    return output_path


def generate_message(amount: str) -> str:
    return f"มีเงินเข้า {amount} บาท"
