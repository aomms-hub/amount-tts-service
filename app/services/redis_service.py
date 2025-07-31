from app.client.redis_client import redis_client

ttl_seconds = 60 * 60

def cache_voice(text: str, audio_url: str):
    key = f"voice:amount:{text}"
    redis_client.set(key, audio_url, ex=ttl_seconds)


def get_cached_voice(text: str):
    key = f"voice:amount:{text}"
    value = redis_client.get(key)
    if value is not None:
        redis_client.expire(key, ttl_seconds)
    return value
