from typing import Any


class Node:
    """
    Posts
    """
    def __init__(self, identify: int, title, media_thumbnail, author, content):
        self.__identify = identify
        self.next = None
        self.prev = None
        self.title = title
        self.media_thumbnail = media_thumbnail
        self.author = author
        self.content = content
    

    @property
    def identify(self):
        return self.__identify


    @identify.setter
    def identify(self, new_id: Any):
        raise Exception('This attribute cannot be changed')
