# from lib.posts import Posts
# from fastapi import FastAPI, Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# # import os
# # import uvicorn
# # from dotenv import load_dotenv


# app = FastAPI()
# # feed = Posts()
# load_dotenv()

# # config
# templates = Jinja2Templates(directory="templates")
# app.mount(
#     "/static",
#     StaticFiles(directory="static"),
#     name="static",
# )

# @app.get("/api/posts")
# async def get_feeds():
#     return feed.get_posts()


# @app.get("api/post/{post_id}")
# async def get_feeds_by_id(post_id: int):
#     post = feed.get_post_by_id(post_id)
#     return post


# @app.get("/")
# async def home(request: Request):
#     return templates.TemplateResponse(
#             "index.html", 
#             {
#                 "request": request,
#                 "posts": feed.get_posts(),
#             }
#         )


# @app.get("/post/{id}")
# async def posts(request: Request, id: int):
#     post = feed.get_post_by_id(id)
#     return templates.TemplateResponse(
#             "post.html",
#             {
#                 "request": request,
#                 "post": post,    
#             }
#         )


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT"), log_level="info")
