from fastapi import APIRouter
from ..Services.core import Fetch
from ..Services.linked_posts import LinkedPosts


router = APIRouter()
fetch_cr = Fetch()
fetch_mal = Fetch()

@router.get("/api/last/crunchyroll")
async def get_lastest_feeds():

    fetch_cr.connect(target=LinkedPosts, source="crunchyroll") 

    last_post_cr = fetch_cr.posts.head

    return fetch_cr.posts.last_node_json(last_post_cr)


@router.get("/api/last/myanimelist")
async def get_lastest_feeds():

    fetch_mal.connect(target=LinkedPosts, source="myanimelist")

    last_post_mal = fetch_mal.posts.head

    return fetch_mal.posts.last_node_json(last_post_mal)
