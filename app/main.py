from fastapi import FastAPI
from app.services.redis_service import get_cached_voice
from app.services.generate_voice_service import generate_voice_amount

app = FastAPI()


@app.get("/")
def root():
    return {"message": "TTS service is running"}


@app.get("/generate_voice")
def generate_voice(amount: str):
    cached = get_cached_voice(amount)
    if cached:
        return {"from_cache": True, "amount": amount, "audio_url": cached}
    audio_url = generate_voice_amount(amount)
    return {
        "from_cache": False,
        "amount": amount,
        "audio_url": audio_url
    }
