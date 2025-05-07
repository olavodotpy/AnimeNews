from lib.api import APIGet

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import uvicorn
from dotenv import load_dotenv


app = FastAPI()
api_response = APIGet()
load_dotenv()

templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

# @app.get("/api/posts")
# async def get_feeds():
#     posts = util.get_all_posts(LinkedPosts)
#     return feed.json()


# @app.get("api/post/{post_id}")
# async def get_feeds_by_id(post_id: int):
#     # post = feed.get_post_by_id(post_id)
#     posts = util.get_all_posts(LinkedPosts)
#     return post


# @app.get("/")
# async def home(request: Request):
#     posts = util.get_all_posts(LinkedPosts)
#     return templates.TemplateResponse(
#             "index.html", 
#             {
#                 "request": request,
#                 "posts": feed.json(),
#             }
#         )


@app.get("/post/{_id}")
async def posts(request: Request, _id: int):
    post = api_response.get_post_by_id(_id)
 
    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": post,    
            }
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT"), log_level="info")
