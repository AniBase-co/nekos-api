import typing

from fastapi import FastAPI, Query

from peewee import *

from .openapi_metadata import tags

from api.database.models.images import Image
from api.v1 import schemas


description = """
# Attribution

Although you are not required to provide attribution, i'd be nice if you did 💕. It motivates me to keep working on the API.

# Wrappers

Python 3: [`AniBase-co/anime-api`](https://github.com/AniBase-co/anime-api)
"""

app = FastAPI(
    title="Nekos API v1",
    description=description,
    version="0.1.0",
    license_info={
        "name": "MIT License",
        "url": "https://github.com/AniBase-co/nekos-api/blob/main/LICENSE"
    },
    openapi_tags=tags
)

@app.get('/')
async def index():
    return {"message": "Welcome to the Nekos API!"}

@app.get('/image/{category}', response_model=typing.Union[schemas.Image, schemas.ImageList])
async def get_random_image(category: Image.Category, amount: int = Query(default=1, gt=0, lt=21)):
    images = Image.select().where(Image.category == category.value).order_by(fn.Random()).limit(amount)
    if amount > 1:
        return schemas.ImageList(images=list(images))
    return images.first()