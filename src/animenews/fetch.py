import feedparser
from .lib.linked_posts import LinkedPosts
from config import url_crunchyroll, default_image


def entries() -> list:
    response = feedparser.parse(url_crunchyroll)
    return response.entries


def fetch_posts(structure: LinkedPosts) -> LinkedPosts:
    linked_posts: LinkedPosts = structure()
    response = entries()
    post_id: int = 1

    # -CACHE-

    for element in response:

        if element.media_thumbnail[0]['url'] == "":
            element.media_thumbnail[0]['url'] = default_image

        linked_posts.append_end_group(
            post_id, element.title, element.media_thumbnail[0]['url'],
            element.author, element.content[0]['value']
        )

        post_id += 1

    return linked_posts
