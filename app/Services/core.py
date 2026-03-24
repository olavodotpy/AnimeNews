from time import sleep
import feedparser
from hashlib import sha256

from .linked_posts import LinkedPosts
from ..Exceptions.CacheFailedError import CacheFailedError
from ..Exceptions.FailedToCommunicateWithTheAPI import FailedToCommunicateWithTheAPI


class Fetch:
    """
    Class responsible for fetching RSS feeds universally. 
    It can be used with Crunchyroll, Anime News Network, or any other feed.
    """
    def __init__(self):
        self.default_img: str = (
            "https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png"
        )

        self.feeds = {
            "crunchyroll": "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss",
            "myanimelist": "https://myanimelist.net/rss/news.xml",
            # "ann": "https://www.animenewsnetwork.com/news/rss.xml?ann-edition=us",      
            # "other": "https://exemplo.com/feed",
        }

        self.posts: LinkedPosts | None = None


    def _generate_guid_sha256(self, entry) -> str:
        """
        Generates a unique and deterministic ID for each post.
        Title + Date
        """
        titulo = entry.get("title", "sem-titulo")
        data = entry.get("published", "") or entry.get("updated", "")
        identificador = f"{titulo}{data}"

        hash_obj = sha256(identificador.encode("utf-8"))
        
        return hash_obj.hexdigest()[:16]


    def _extract_post(self, entry, source: str):
        """
        Extracts data from a feed entry securely.
        It works even if the feed has different fields.
        """
        image = self.default_img
        try:
            if hasattr(entry, "media_thumbnail") and entry.media_thumbnail:
                image = entry.media_thumbnail[0].get("url") or self.default_img

            elif hasattr(entry, "media_content") and entry.media_content:
                image = entry.media_content[0].get("url") or self.default_img
        except:
            image = self.default_img

        return {
            "guid": self._generate_guid_sha256(entry),
            "title": entry.get("title", "Sem título"),
            "image": image,
            "author": entry.get("author", "Desconhecido"),
            "content": entry.get("content", [{}])[0].get("value", "")
                    or entry.get("description", "")
                    or entry.get("summary", ""),
            "link": entry.get("link", ""),
        }


    def _fetch_feed(self, url: str):
        """It parses the feed while handling errors."""
        response = feedparser.parse(url)

        if response.get("bozo", 0):
            exception = response.get("bozo_exception", "Unknown error")
            raise FailedToCommunicateWithTheAPI(f"Feed parser falhou: {exception}")

        if response.get("status") and response.status != 200:
            raise FailedToCommunicateWithTheAPI(f"HTTP error: status {response.status}")

        return response.entries


    def connect(self, target: LinkedPosts, source: str = "crunchyroll"):
        """ 
        It connects and loads posts from a specific feed.
        """
        linked_posts = target()

        try:
            url = self.feeds[source]
            entries = self._fetch_feed(url)
        except Exception as e:
            linked_posts.append(404, f"<ERROR> {source.upper()} API", None, None, f"Error: {e}", "")
            self.posts = linked_posts
            return

        for entry in entries:
            post_data = self._extract_post(entry, source)

            linked_posts.append(
                post_data["guid"],
                post_data["title"],
                post_data["image"],
                post_data["author"],
                post_data["content"],
                post_data["link"],
            )
        self.posts = linked_posts


    def update(self, target: LinkedPosts, source: str = "crunchyroll", timer: int=900):
        """
        Update the feeds periodically.
        For now, just Crunchyroll. Later we can do multiple feeds.
        """
        while True:
            sleep(timer)
            try:
                self.connect(target=target, source=source)
            except:
                raise CacheFailedError
