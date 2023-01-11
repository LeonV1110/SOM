class InvalidDestination(Exception):
    def __init__(self, message="You have selected an invalid destination, please try again"):
        self.message = message
        super().__init__(self.message)
