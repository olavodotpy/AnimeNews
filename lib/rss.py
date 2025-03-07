import feedparser


response = feedparser.parse("https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss")

data = response.entries

class Post:

    def __init__(self) -> None:
        pass


    def get_post(self) -> list:

        list_post = list()

        count_id: int = 1

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

