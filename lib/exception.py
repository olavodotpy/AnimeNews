class NodeNotFoundError(Exception):
    """Exeception for nodes not found."""

    def __init__(self, message='No node was found during program execution.') -> None:
        self.message = message
        super().__init__(self.message)
