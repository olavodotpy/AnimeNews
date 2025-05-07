from .node import Node
from .exception import NodeNotFoundError

# from .formatter import Formatter


class LinkedPosts:

    def __init__(self) -> None: 
        self.head = None
        self.tail = None
        self.hash_table = dict() 

    def append_post(self, identify: int, title: str, 
                    media_thumbnail: str, author: str, content: str,
        ):
        """"""
        new_node = Node(identify, title, media_thumbnail, author, content)

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.identify] = new_node
        else:
            self.hash_table[new_node.identify] = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    
    def json(self):
        """"""
        pass


    def search_id(self, _id: int):
        """"""
        node_pointer = self.hash_table.get(_id)

        if self.head is None or _id > 50:
            raise NodeNotFoundError

        _dict = {
            "id": node_pointer.identify,
            "title": node_pointer.title,
            "media": node_pointer.media_thumbnail,
            "author": node_pointer.author,
            "content": node_pointer.content,
        }

        return _dict


    def display(self):
        """"""
        if self.head is None:
            raise NodeNotFoundError
        
        current = self.head

        while current:

            print(current.identify)
            print(current.title)
            print(current.media_thumbnail)
            print(current.author)
            print(current.content)
            print()
            current = current.next


    def display_backwards(self):
        """"""
        if self.head is None:
            raise NodeNotFoundError
        
        current = self.tail

        while current:

            print(current.identify)
            print(current.title)
            print(current.media_thumbnail)
            print(current.author)
            print(current.content)
            print()
            current = current.prev
