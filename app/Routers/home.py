from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates

from ..Services.core import Fetch
from ..Services.linked_posts import LinkedPosts

from contextlib import asynccontextmanager 
from threading import Thread

fetch = Fetch()

@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch.connect(target=LinkedPosts, source="crunchyroll")
    Thread(target=fetch.update, args=(LinkedPosts,"crunchyroll",), kwargs={"timer": 100}, daemon=True).start()
    
    yield


router = APIRouter(lifespan=lifespan)


templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    response = fetch.posts.json()

    return templates.TemplateResponse(
            "home.html", 
            {
                "request": request,
                "posts": response,
            }
        )


@router.get("/post/{post_guid}")
async def post(request: Request, post_guid: str):
    response = fetch.posts.search(post_guid)

    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": response,    
            }
        )
