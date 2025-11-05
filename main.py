from .src.animenews.lib.linked_posts import LinkedPosts

from fastapi import Request, HTTPException
import feedparser

from .config import app, Request, templates, default_img, crunchyroll_api

import os
import uvicorn
from dotenv import load_dotenv
from threading import Thread
from time import sleep 

load_dotenv()

linked_posts = None

def get_cached_posts():
    global linked_posts
    if linked_posts is None:
        linked_posts = fetch_posts(LinkedPosts)
    return linked_posts

def refresh_cache(t: int=300):
    global linked_posts
    while True:
        sleep(t)
        linked_posts = None
        print("\tCache refreshed!")

def entries() -> list:
    try:
        response = feedparser.parse(crunchyroll_api)
    except Exception as e:
        print(f"\t[ERROR]: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch crunchyroll RSS")

    return response.entries

def fetch_posts(structure: LinkedPosts) -> LinkedPosts:
    linked_posts: LinkedPosts = structure()

    response = entries()

    post_id: int = 1

    for element in response:
        if element.media_thumbnail[0]['url'] == "":
            element.media_thumbnail[0]['url'] = default_img

        linked_posts.append(
            post_id, element.title, element.media_thumbnail[0]['url'],
            element.author, element.content[0]['value']
        )

        post_id += 1

    return linked_posts

@app.get("/api/posts")
async def get_feeds(): 
    posts = get_cached_posts()
    response = posts.json_node_list()

    return response

@app.get("api/post/{post_id}")
async def get_feeds_by_id(post_id: int):
    post = get_cached_posts()
    response_post_by_id = post.search_id(post_id)

    return response_post_by_id

@app.get("/")
async def home(request: Request):
    posts = get_cached_posts()
    response = posts.json_node_list()

    return templates.TemplateResponse(
            "index.html", 
            {
                "request": request,
                "posts": response,
            }
        )

@app.get("/post/{post_id}")
async def posts(request: Request, post_id: int):
    post = get_cached_posts()
    response = post.search_id(post_id)

    return templates.TemplateResponse(
            "post.html",
            {
                "request": request,
                "post": response,    
            }
        )

Thread(target=refresh_cache, daemon=True).start()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT"), log_level="info")
