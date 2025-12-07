class InvalidPostID(Exception):
    """exception if id is changed or invalid"""

    def __init__(self, message='The index of posts cannot be changed!!') -> None:
        self.message = message
        super().__init__(self.message)