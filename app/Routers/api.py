from fastapi import APIRouter
from ..Services.core import Fetch
from ..Services.linked_posts import LinkedPosts


router = APIRouter()
fetch = Fetch()


@router.get("/api/post/crunchyroll")
async def get_feeds_crunchyroll():
    
    fetch.connect(target=LinkedPosts, source="crunchyroll") 

    last_post = fetch.posts.head

    return fetch.posts.last_node_json(last_post)


@router.get("/api/post/myanimelist")
async def get_feeds_myanimelist():
    
    fetch.connect(target=LinkedPosts, source="myanimelist") 

    last_post = fetch.posts.head

    return fetch.posts.last_node_json(last_post)
