from .node import Node
from ..Exceptions.NodeNotFoundError import NodeNotFoundError
from ..Exceptions.InvalidPostGUID import InvalidPostGUID
from ..Schemas.schema import PostSchema

from ..Utils.formatter import formatter_text



class LinkedPosts:
    """
    A Link Posts class with the attributes head, tail, and hash_table.
    The structure for loading the template is generated.
    """
    def __init__(self) -> None: 
        self.head = None
        self.tail = None
        self.hash_table = dict()

    def append(self, source: str ,guid: str, title: str | None, image: str | None,
                author: str | None, content: str | None, description: str | None,
                link: str | None, url: str | None, cr_color: str | None, mal_color: str | None
        ):
        """The append method adds the posts in node format to LinkedPosts and caches them using the hash_table dictionary."""
        if guid in self.hash_table:
            raise InvalidPostGUID

        new_node = Node(source, guid, title, image, author, content,
                        description, link, url, cr_color, mal_color,
                    )

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.guid] = new_node
        else:
            self.hash_table[new_node.guid] = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        if len(self.hash_table) == 100:
            self.hash_table.clear()


    def prepend(self, source: str ,guid: str, title: str | None, image: str | None,
                author: str | None, content: str | None, description: str | None,
                link: str | None, url: str | None, cr_color: str | None, mal_color: str | None
        ):
        if guid in self.hash_table:
            raise InvalidPostGUID

        new_node = Node(source, guid, title, image, author, content,
                        description, link, url, cr_color, mal_color,
                    )

        if self.head is None:
            self.head = self.tail = new_node
            self.hash_table[new_node.guid] = new_node
            return

        self.hash_table[new_node.guid] = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        if len(self.hash_table) == 100:
            self.hash_table.clear()


    def last_node_json(self, node: Node = None) -> list:
        current = node

        post = PostSchema(
            source=current.source,
            guid=current.guid,
            title=current.title,
            image=current.image,
            author=current.author,
            content=current.content,
            description=current.description,
            link=current.link,
            url=current.url,
            cr_color=current.cr_color,
            mal_color=current.mal_color,
        )

        return post.model_dump()


    def json(self) -> list:
        json_list = []
        current = self.head

        while current:
            post = PostSchema(
                source=current.source,
                guid=current.guid,
                title=current.title,
                image=current.image,
                author=current.author,
                content=current.content,
                description=current.description,
                link=current.link,
                url=current.url,
                cr_color=current.cr_color,
                mal_color=current.mal_color,
            )

            post_structure = post.model_dump()
            json_list.append(post_structure)
            
            current = current.next

        return json_list


    def search(self, guid_requested: str) -> dict:
        if guid_requested not in self.hash_table:
            raise NodeNotFoundError

        response = self.last_node_json(self.hash_table[guid_requested])

        return response


    def display(self):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head

        while current:
            print(current.guid)
            print(current.title)
            print(current.image)
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
            print(current.image)
            print(current.link)
            print()
            current = current.prev


    def is_full(self):
        if self.head != None:
            return True
