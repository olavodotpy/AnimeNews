from fastapi import APIRouter
from ..Models.core import Fetch
from ..Models.linked_posts import LinkedPosts

router = APIRouter()
fetch = Fetch()


@router.get("/api/posts")
async def get_feeds():
    fetch.connect(LinkedPosts) 
    return fetch.posts.json()

@router.get("api/post/{post_id}")
async def get_feeds_by_id(post_id: int):
    
    return fetch.posts.search(post_id)
