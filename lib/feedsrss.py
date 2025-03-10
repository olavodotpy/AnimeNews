import feedparser


RSS_URL = "https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss"

def get_parser(rss_url):
    response = feedparser.parse(rss_url)
    return response.entries


class Posts:

    def __init__(self) -> None:
        pass


    def get_posts(self) -> list:

        list_post = list()

        count_id: int = 1

        data = get_parser(RSS_URL)

        for element in data:

            result = {
                "id": count_id,
                "title": f'{element.title}',
                "media": f'{element.media_thumbnail[0]['url']}',
                "description": f'{element.description}',
                "content": f'{element.content[0]['value']}',
            }
            
            list_post.append(result)
            count_id += 1

        
        return list_post 


    def get_post_by_id(self, access_id: int):

        if access_id > 50 or access_id <= 0 or access_id is int:
            return {"error": "id exceeded or invalid"}

        all_posts = self.get_posts()

        for post in all_posts:
            if access_id == post['id']:
                return dict(post)
