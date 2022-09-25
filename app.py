from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from api.app import app as api_app


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    # Return a coming soon message
    return templates.TemplateResponse('index.html', {'request': request})


app.mount('/static', StaticFiles(directory="static"), name="static-files")
app.mount('/api', api_app, name="api")