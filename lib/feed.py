import feedparser


URL = feedparser.parse("https://cr-news-api-service.prd.crunchyrollsvc.com/v1/pt-BR/rss")

link_content = URL.entries

for element in link_content:
    print(f"{element.title}\n")
    print(f"{element.category}\n")
    print(f"{element.description}\n")
    print(f"{element.content[0]['value']}\n")

