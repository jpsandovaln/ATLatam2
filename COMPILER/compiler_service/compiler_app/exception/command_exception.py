from ..exception.compiler_exception import CompilerException


class CommandException(CompilerException):
    def __init__(self, message, status, code):
        super().__init__(message, status, code)
