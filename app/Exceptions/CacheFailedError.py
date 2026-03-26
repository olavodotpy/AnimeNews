class CacheFailedError(Exception):
    """Exception if the cache does not function correctly."""
    def __init__(self, message='The cache cannot be implemented.') -> None:
        self.message = message
        super().__init__(self.message)
