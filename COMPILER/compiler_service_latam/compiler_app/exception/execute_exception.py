from ..exception.compiler_exception import CompilerException


class ExecuteException(CompilerException):
    def __init__(self, message):
        self.message = message
        self.status = "406"
        self.code = "Latam-02-12548"
        super().__init__(self.message, self.status, self.code)
