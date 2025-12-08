from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..Models.services import FetchService
from ..Models.linked_posts import LinkedPosts

templates = Jinja2Templates(directory="templates")
fetch = FetchService()
router = APIRouter()

@router.get("/")
async def home(request: Request):
    fetch.add_posts(LinkedPosts)
    response = fetch.posts.json()

    return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "posts": response,
            }
        )

@router.get("/post/{post_id}")
async def posts(request: Request, post_id: int):
    fetch.add_posts(LinkedPosts)
    response = fetch.posts.search(post_id)

    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": response,    
            }
        )
