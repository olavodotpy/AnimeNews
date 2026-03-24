from ..Exceptions.InvalidPostGUID import InvalidPostGUID

class Node:
    """
    Posts
    """

    def __init__(self, guid: str, title: str | None, media_thumbnail: str | None,
                author: str | None, content: str, link: str,
        ):
        self.next = None
        self.prev = None
        self.__guid = guid
        self.title = title
        self.media_thumbnail = media_thumbnail
        self.author = author
        self.content = content
        self.link = link


    @property
    def guid(self):
        return self.__guid


    @guid.setter
    def guid(self, new_guid: str):
        raise InvalidPostGUID
