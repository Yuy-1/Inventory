from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

add.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*']
    allow_headers=['*']
)

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

@app.get('/products')
def all():
    return Product.all_pks()

@app.post('/products')
def create(product: Product):
    return product.save()