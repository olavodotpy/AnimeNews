from .node import Node
from ..Exceptions.NodeNotFoundError import NodeNotFoundError
from ..Exceptions.InvalidPostGUID import InvalidPostGUID

from ..Utils.formatter import formatter_text

class LinkedPosts:

    def __init__(self) -> None: 
        self.head = None
        self.tail = None
        self.hash_table = dict() 


    def append(self, guid: str, title: str | None, media_thumbnail: str | None,
            author: str | None, content: str, link: str,
        ):
        if guid in self.hash_table:
            raise InvalidPostGUID

        new_node = Node(guid, title, media_thumbnail, author, content, link)

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.guid] = new_node
        else:
            self.hash_table[new_node.guid] = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def prepend(self, guid: str, title: str | None, media_thumbnail: str | None,
                author: str | None, content: str, link: str,
        ):
        if guid in self.hash_table:
            raise InvalidPostGUID

        new_node = Node(guid, title, media_thumbnail, author, content, link)

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.guid] = new_node
            return

        self.hash_table[new_node.guid] = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def json(self, node=None) -> list:
        json_list = []

        current = self.head if node is None else node

        while current:
            post_structure = {
                "guid": current.guid,
                "title": current.title,
                "media": current.media_thumbnail,
                "author": current.author,
                "content": formatter_text(current.content),
                "link": current.link,
            }

            json_list.append(post_structure)
            current = current.next

        return json_list


    def search(self, guid_requested: str) -> dict:
        if guid_requested not in self.hash_table:
            raise NodeNotFoundError

        response = self.json(self.hash_table[guid_requested])[0]

        return response


    def display(self):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head

        while current:
            print(current.guid)
            print(current.title)
            print(current.media_thumbnail)
            print(current.author)
            print(current.content)
            print(current.link)
            print()
            current = current.next


    def display_backwards(self):
        if self.head is None:
            print("List is empty!")
            return
        
        current = self.tail

        while current:
            print(current.guid)
            print(current.title)
            print(current.media_thumbnail)
            print(current.author)
            print(current.content)
            print(current.link)
            print()
            current = current.prev


    def is_full(self):
        if self.head != None:
            return True
