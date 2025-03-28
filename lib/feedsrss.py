import feedparser
from .formatter import Formatter

class Posts:

    def __init__(self) -> None:
        self.RSS_URL = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss"
        self.ALT_IMG_URL = "https://woorkup.com/wp-content/uploads/2014/08/wordpress-rss-feed-with-images.png"


    def get_parser(self):
        response = feedparser.parse(self.RSS_URL)
        return response.entries


    def set_posts(self) -> list:
        list_post = list()
        count_id: int = 1
        data = self.get_parser()

        for element in data:
            if element.media_thumbnail[0]['url'] == "":
                element.media_thumbnail[0]['url'] = self.ALT_IMG_URL

            result = {
                "id": count_id,
                "title": f'{element.title}',
                "media": f'{element.media_thumbnail[0]['url']}',
                "content": f'{element.content[0]['value']}',
                "author": f'{element.author}',
            }
            
            list_post.append(result)
            count_id += 1
        
        return list_post 
    

    def get_posts(self):
        result_posts = self.set_posts()

        for post in result_posts:
            form = Formatter(post['content'])
            post["initial_content"] = f'{form.content_filters("RELACIONADO:")}'
            post["iddle_content"] = f'{form.content_filters("Fonte:")}'
            post["final_content"] = f'{" ".join(form.word_group)}'
            del post['content']

        return result_posts


    def get_post_by_id(self, access_id: int):
        if access_id > 50 or access_id <= 0 or access_id is int:
            return {"error": "id exceeded or invalid"}

        all_posts = self.get_posts()

        for post in all_posts:
            if access_id == post['id']:
                return dict(post)
