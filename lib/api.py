import feedparser
from .linkedPosts import LinkedPosts


class APIGet:
    
    def __init__(self):
        self.url_crunchyroll = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss"
        self.default_image = "https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png"   


    def get_entries(self) -> list:
        response = feedparser.parse(self.url_crunchyroll)
        return response.entries


    def get_posts(self):
        list_posts = LinkedPosts()
        
        # -CACHE-

        data = self.get_entries()
        count_id: int = 1
        for item in data:

            list_posts.append_post(
                count_id, item.title, item.media_thumbnail[0]['url'],
                item.author, item.content[0]['value']
            )

            count_id += 1

        return list_posts


    def get_post_by_id(self, _id: int):
        # issues -> ID error when adding "new post" #7
        result = self.get_posts()
        # issues -> ID error when adding "new post" #7
        return result.search_id(_id)
