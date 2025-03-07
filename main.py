from lib import feedsrss
from fastapi import FastAPI


app = FastAPI()
rss = feedsrss.Post()



@app.get("/posts")
async def get_feeds():
    return rss.get_posts()


@app.get("/post/{post_id}")
async def get_feeds_by_id(post_id: int):
    post = rss.get_post_by_id(post_id)

    return post
