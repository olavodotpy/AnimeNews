from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .Routers import api, home, feed


app = FastAPI()

STATIC_URL = 'static'

app.mount(
    "/static",
    StaticFiles(directory=STATIC_URL),
    name="static",
)

app.include_router(api.router)
app.include_router(home.router)
app.include_router(feed.router)
