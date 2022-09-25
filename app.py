from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse

import random

from api.app import app as api_app


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    # Return a coming soon message
    return templates.TemplateResponse('index.html', {'request': request, 'catgirl': f'catgirl-{random.randint(1, 9)}.png'})

@app.get('/media/{path:path}', response_class=FileResponse)
async def get_media(path: str):
    return FileResponse(f'media/{path}')
    

app.mount('/static', StaticFiles(directory="static"), name="static-files")
app.mount('/api', api_app, name="api")