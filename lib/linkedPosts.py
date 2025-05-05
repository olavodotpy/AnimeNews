from node import Node
# from .formatter import Formatter


class LinkedPosts:

    def __init__(self) -> None: 
        self.head = None
        self.tail = None


    def append_post(self, identify: int, title: str, 
                    media_thumbnail: str, author: str, content: str,
        ):
        new_node = Node(identify, title, media_thumbnail, author, content)
        

        # HASH TABLE FOR SEARCH
        # using pure Node


        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    
    def json(self):
        pass


    def get_post_by_id(self):
        pass


    def display(self):
        if self.head is None:
            print('list is empty')
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
            print('list is empty')
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
