class ParameterException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.status = "405"
        self.code = code
        super().__init__(self.message)

