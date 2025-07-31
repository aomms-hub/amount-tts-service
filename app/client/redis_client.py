import os
from dotenv import load_dotenv
import redis

load_dotenv()

REDIS_URL = os.getenv("UPSTASH_REDIS_REST_URL")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)
