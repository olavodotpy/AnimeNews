from lib import rss
from fastapi import FastAPI


app = FastAPI()


@app.get("/post")
async def post_news():
    content = rss.Post()
    return content.get_post()
