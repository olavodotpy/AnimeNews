from os import sync
from typing import Union

from fastapi import FastAPI


app = FastAPI()

dataBase = dict()

@app.get("/")
async def root():
    return {"ALERT": "Hello, World"}

