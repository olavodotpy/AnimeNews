from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .Routers import api
from .Models.core import Fetch
from .Models.linked_posts import LinkedPosts

from contextlib import asynccontextmanager 
from threading import Thread

# production:

# import os
# import uvicorn
# from dotenv import load_dotenv

# load_dotenv()

fetch = Fetch()

@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch.connect(LinkedPosts)
    Thread(target=fetch.update, args=(LinkedPosts,), kwargs={"timer": 100}, daemon=True).start()
    
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api.router)

templates = Jinja2Templates(directory="templates")

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


# production:

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT"), log_level="info")
