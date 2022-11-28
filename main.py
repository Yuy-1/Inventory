from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host="redis-17048.c57.us-east-1-4.ec2.cloud.redislabs.com:17048"
    port=17048,
    password="0bmtcbHl5EvAJLlm675aYuap5Fyd5Jtl",
    decode_response=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

