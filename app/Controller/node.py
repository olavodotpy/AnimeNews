from ..Exceptions.InvalidPostID import InvalidPostID

class Node:
    """
    Posts
    """
    def __init__(self, identify: int, title: str, media_thumbnail: str | None, author: str, content: str):
        self.next = None
        self.prev = None
        self.__identify = identify
        self.title = title
        self.media_thumbnail = media_thumbnail
        self.author = author
        self.content = content

    @property
    def identify(self):
        return self.__identify

    @identify.setter
    def identify(self, new_id: int):
        raise InvalidPostID
