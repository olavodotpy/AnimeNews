from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates

from ..Services.core import Fetch
from ..Services.linked_posts import LinkedPosts

from contextlib import asynccontextmanager 
from threading import Thread



fetch = Fetch()

@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch.connect(target=LinkedPosts, source="myanimelist")
    Thread(target=fetch.update, args=(LinkedPosts,"myanimelist",), kwargs={"timer": 100}, daemon=True).start()
    
    yield


router = APIRouter(lifespan=lifespan)


templates = Jinja2Templates(directory="app/templates")

@router.get("/feeds")
async def home(request: Request):
    response = fetch.posts.json()

    return templates.TemplateResponse(
            "feeds.html", 
            {
                "request": request,
                "posts": response,
            }
        )
