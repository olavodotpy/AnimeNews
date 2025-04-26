from typing import Any

class NodeNotFoundError(Exception):
    """Exeception for nodes not found."""

    def __init__(self, message='Node not Found in the operation.') -> None:
        self.message = message
        super().__init__(self.message)


class Node:
    """
    Posts
    """
    def __init__(self, identify: int, title, media_thumbnail, author, content):
        self.__identify = identify
        self.next = None
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
