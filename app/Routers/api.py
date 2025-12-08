from fastapi import APIRouter
from ..Models.services import FetchService
from ..Models.linked_posts import LinkedPosts

router = APIRouter()
fetch = FetchService()

@router.get("/api/posts")
async def get_feeds(): 
    fetch.add_posts(LinkedPosts)
    
    return fetch.list_posts.json()

@router.get("api/post/{post_id}")
async def get_feeds_by_id(post_id: int):
    fetch.add_posts(LinkedPosts)
    
    return fetch.list_posts.search(post_id)
