class ExecuteException(Exception):
    def __init__(self, message):
        self.message = message
        self.status = "406"
        self.code = "Latam-02-12548"
        super().__init__(self.message)
