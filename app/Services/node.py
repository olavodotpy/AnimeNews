from ..Exceptions.InvalidPostGUID import InvalidPostGUID



class Node:
    """
    Posts
    """
    def __init__(self, source: str, guid: str, title: str | None, image: str | None,
                author: str | None, content: str | None, description: str, link: str | None,
                url: str | None, cr_color: str | None, mal_color: str | None
        ):
        self.next = None
        self.prev = None
        self.source = source
        self.__guid = guid
        self.title = title
        self.image = image
        self.author = author
        self.content = content
        self.description = description
        self.link = link
        self.url = url
        self.cr_color = cr_color
        self.mal_color = mal_color


    @property
    def guid(self):
        return self.__guid


    @guid.setter
    def guid(self, new_guid: str):
        raise InvalidPostGUID
