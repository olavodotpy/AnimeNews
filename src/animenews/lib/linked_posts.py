from .node import Node
from .exception import NodeNotFoundError

from .formatter import split_dot


class LinkedPosts:

    def __init__(self) -> None: 
        self.head = None
        self.tail = None
        self.hash_table = dict() 


    def append_end_group(self, identify: int, title: str, 
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

    
    def append_start_group(self, identify: int, title: str, 
                    media_thumbnail: str, author: str, content: str,
        ):
        """"""
        new_node = Node(identify, title, media_thumbnail, author, content)

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.identify] = new_node
            return

        self.hash_table[new_node.identify] = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    
    def json(self):
        """"""
        json_lists = list()
        current = self.head

        while current:

            json_structure = {
                "id": current.identify,
                "title": current.title,
                "media": current.media_thumbnail,
                "author": current.author,
                "content": split_dot(current.content),
            }

            json_lists.append(json_structure)
            current = current.next

        return json_lists
        

    def search_id(self, id_requested: int):
        """"""
        node_pointer = self.hash_table.get(id_requested)

        if self.head is None:
            raise NodeNotFoundError


        json_structure = {
            "id": node_pointer.identify,
            "title": node_pointer.title,
            "media": node_pointer.media_thumbnail,
            "author": node_pointer.author,
            "content": split_dot(node_pointer.content),
        }

        return json_structure


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
