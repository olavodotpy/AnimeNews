from fastapi import HTTPException
from .linked_posts import LinkedPosts

import feedparser


class FetchService:

    def __init__(self) -> None:
        self.crunchyroll_api: str = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss"
        self.default_img: str = "https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png"
        self.posts: LinkedPosts = None


    def entries(self) -> list:
        try:
            response = feedparser.parse(self.crunchyroll_api)
        except Exception as e:
            print(f"\t[ERROR]: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch crunchyroll RSS")

        return response.entries


    def add_posts(self, structure: LinkedPosts):
        linked_posts = structure()
        response = self.entries()

        post_id: int = 1

        for element in response:
            if element.media_thumbnail[0]['url'] == "":
                element.media_thumbnail[0]['url'] = self.default_img

            linked_posts.append(
                post_id, element.title, element.media_thumbnail[0]['url'],
                element.author, element.content[0]['value']
            )

            post_id += 1

        self.posts = linked_posts
