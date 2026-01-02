class FailedToCommunicateWithTheAPI(Exception):
    """Error with the client API"""

    def __init__(self, message='The server was unable to complete contact with the API client.') -> None:
        self.message = message
        super().__init__(self.message)
