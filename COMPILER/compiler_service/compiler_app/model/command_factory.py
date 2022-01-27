from .java_command import JavaCommand
from .python_command import PythonCommand
from .node_command_adapter import NodeCommandAdapter


class CommandFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_instance(language, file):
        if language == "java":
            command = JavaCommand()
        if language == "python":
            command = PythonCommand()
        if language == "node":
            command = NodeCommandAdapter()
        return command
