from lib.linked_posts import LinkedPosts
from fetch import fetch_posts

from fastapi import Request

from config import app, Request, templates

import os
import uvicorn
from dotenv import load_dotenv


load_dotenv()

@app.get("/api/posts")
async def get_feeds(): 
    group_posts = fetch_posts(LinkedPosts)
    response = group_posts.json()
    return response


@app.get("api/post/{post_id}")
async def get_feeds_by_id(post_id: int):
    group_posts = fetch_posts(LinkedPosts)
    post_by_id = group_posts.search_id(post_id)
    return post_by_id


@app.get("/")
async def home(request: Request):
    group_posts = fetch_posts(LinkedPosts)
    post_cards = group_posts.json()

    return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "posts": post_cards,
            }
        )


@app.get("/post/{post_id}")
async def posts(request: Request, post_id: int):
    group_posts = fetch_posts(LinkedPosts)
    post_select = group_posts.search_id(post_id)

    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": post_select,    
            }
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT"), log_level="info")
