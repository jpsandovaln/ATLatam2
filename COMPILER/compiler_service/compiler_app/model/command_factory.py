from .java_command import JavaCommand
from .python_command import PythonCommand


class CommandFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_instance(language):
        if language == "java":
            command = JavaCommand()
        if language == "python":
            command = PythonCommand()
        return command
