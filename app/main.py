from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from .Routers import api, web
from .Models.core import Fetch

# import os
# import uvicorn
# from dotenv import load_dotenv

# load_dotenv()
app = FastAPI()
fetch = Fetch()

app.include_router(api.router)
app.include_router(web.router)


STATIC_URL = 'static'

app.mount(
    "/static",
    StaticFiles(directory=STATIC_URL),
    name="static",
)

#production:

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT"), log_level="info")
