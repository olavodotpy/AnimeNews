from fastapi import APIRouter, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from ..Models.core import Fetch
from ..Models.linked_posts import LinkedPosts

templates = Jinja2Templates(directory="templates")

fetch = Fetch()
fetch.connect(LinkedPosts)
router = APIRouter()

@router.get("/")
async def home(request: Request, background_tasks: BackgroundTasks):
    background_tasks.add_task(fetch.update, LinkedPosts)
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
    response = fetch.posts.search(post_id)

    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": response,    
            }
        )
