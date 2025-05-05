import feedparser

class Utilities:
    
    def __init__(self):
        self.url_crunchyroll = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss"
        self.default_image = "https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png"
    

    def get_parser(self) -> list:
        response = feedparser.parse(self.url_crunchyroll)
        return response.entries


    def append_all_posts(self, structure):
        posts_linked_list = structure()
        
        # -CACHE-

        data = self.get_parser()

        count_id: int = 1

        for item in data:

            posts_linked_list.append_post(
                count_id, item.title, item.media_thumbnail[0]['url'],
                item.content[0]['value'], item.author
            )

            count_id += 1

        return posts_linked_list
