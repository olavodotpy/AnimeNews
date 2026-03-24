from fastapi import APIRouter
from ..Services.core import Fetch
from ..Services.linked_posts import LinkedPosts


router = APIRouter()
fetch = Fetch()

fetch.connect(target=LinkedPosts, source="crunchyroll") 

@router.get("/api/posts")
async def get_feeds():

    return fetch.posts.json()


@router.get("/api/post/{post_guid}")
async def get_feeds_by_id(post_guid: str):

    return fetch.posts.search(post_guid)
