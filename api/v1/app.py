from fastapi import FastAPI

from .openapi_metadata import tags


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