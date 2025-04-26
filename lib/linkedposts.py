from node import Node, NodeNotFoundError
# from .formatter import Formatter


class LinkedPosts:

    def __init__(self) -> None: 
        self.head = None


    def append_post(self, identify: int, title: str, 
                    media_thumbnail: str, author: str, content: str,
        ):
        new_node = Node(identify, title, media_thumbnail, author, content)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node


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
