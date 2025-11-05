from .node import Node
from .exception import NodeNotFoundError

from .formatter import formatter_text

class LinkedPosts:

    def __init__(self) -> None: 
        self.head = None
        self.tail = None
        self.hash_table = dict() 

    def append(self, identify: int, title: str, 
                    media_thumbnail: str | None, author: str, content: str,
        ):

        if identify in self.hash_table:
            raise ValueError(f"ID {identify} already exists.")

        new_node = Node(identify, title, media_thumbnail, author, content)

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.identify] = new_node
        else:
            self.hash_table[new_node.identify] = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, identify: int, title: str, 
                    media_thumbnail: str, author: str, content: str,
        ):

        if identify in self.hash_table:
            raise ValueError(f"ID {identify} already exists.")

        new_node = Node(identify, title, media_thumbnail, author, content)

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.identify] = new_node
            return

        self.hash_table[new_node.identify] = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def json_node_list(self, node=None) -> list:
        json_list = []

        current = self.head if node is None else node

        while current:
            json_structure = {
                "id": current.identify,
                "title": current.title,
                "media": current.media_thumbnail,
                "author": current.author,
                "content": formatter_text(current.content),
            }

            json_list.append(json_structure)
            current = current.next

        return json_list

    def search_id(self, id_requested: int) -> dict:

        if id_requested not in self.hash_table:
            raise NodeNotFoundError
        
        node_pointer = self.hash_table.get(id_requested)

        response = self.json_node_list(node_pointer)[0]

        return response

    def display(self):
        if self.head is None:
            print("List is empty!")
            return

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
        if self.head is None:
            print("List is empty!")
            return
        
        current = self.tail

        while current:
            print(current.identify)
            print(current.title)
            print(current.media_thumbnail)
            print(current.author)
            print(current.content)
            print()
            current = current.prev
