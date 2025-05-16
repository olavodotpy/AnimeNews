from fastapi import FastAPI, Request # necessary
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    StaticFiles(directory="./static"),
    name="static",
)
templates = Jinja2Templates(directory="templates")


url_crunchyroll: str = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss"
default_image: str = "https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png"
