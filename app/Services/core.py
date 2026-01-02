from .linked_posts import LinkedPosts
from ..Exceptions.CacheFailedError import CacheFailedError
from ..Exceptions.FailedToCommunicateWithTheAPI import FailedToCommunicateWithTheAPI
from time import sleep
import feedparser


class Fetch:

    def __init__(self) -> None:
        self.crunchyroll_api: str = 'https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss'
        self.default_img: str = 'https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png'
        self.posts: LinkedPosts | None  = None


    def entries(self) -> list:
        response = feedparser.parse(self.crunchyroll_api)

        if response.get('bozo', 0):
            exception = response.get('bozo_exception', 'Unknown error')
            raise FailedToCommunicateWithTheAPI(f"Feed parser failed: {str(exception)}")
        
        if 'status' in response and response.status != 200:
            raise FailedToCommunicateWithTheAPI(f"HTTP error: status {response.status}")

        return response.entries


    def connect(self, target: LinkedPosts):
        linked_posts = target()
        try:
            response = self.entries()
        except:
            linked_posts.append(404, "<ERROR> CLIENT SERVER API", None, None, "Error: Not Found")
            self.posts = linked_posts
            return

        post_id: int = 1

        for e in response:
            if e.media_thumbnail[0]['url'] == "" or e.media_thumbnail[0]['url'] == None :
                e.media_thumbnail[0]['url'] = self.default_img

            linked_posts.append(
                post_id, e.title, e.media_thumbnail[0]['url'],
                e.author, e.content[0]['value']
            )

            post_id += 1

        self.posts = linked_posts


    def update(self, target: LinkedPosts, timer: int=900):
        while True:
            sleep(timer)
            self.connect(target=LinkedPosts)
