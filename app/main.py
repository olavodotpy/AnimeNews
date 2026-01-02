from typing import Any

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .Routers import api
from .Services.core import Fetch
from .Services.linked_posts import LinkedPosts

from contextlib import asynccontextmanager 
from threading import Thread


fetch = Fetch()

@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch.connect(target=LinkedPosts)
    Thread(target=fetch.update, args=(LinkedPosts,), kwargs={"timer": 100}, daemon=True).start()
    
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api.router)

templates = Jinja2Templates(directory="app/templates")

STATIC_URL = 'static'

app.mount(
    "/static",
    StaticFiles(directory=STATIC_URL),
    name="static",
)


@app.get("/")
async def home(request: Request):
    response = fetch.posts.json()

    return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "posts": response,
            }
        )

@app.get("/post/{post_id}")
async def posts(request: Request, post_id: int):
    response = fetch.posts.search(post_id)

    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": response,    
            }
        )
