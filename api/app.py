from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .v1.app import app as api_v1


app = FastAPI()


@app.get('/')
async def root():
    return RedirectResponse('endpoints')


@app.get('/endpoints')
async def endpoints():
    return {
        "v1": {
            "endpoints": [
                
            ]
        }
    }


app.mount('/v1', api_v1, name='api-v1')