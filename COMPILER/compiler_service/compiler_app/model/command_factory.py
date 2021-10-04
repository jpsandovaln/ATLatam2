from .java_command import JavaCommand
from .java_command_proxy import JavaCommandProxy
from .python_command import PythonCommand
from .node_command_adapter import NodeCommandAdapter


class CommandFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_instance(language):
        if language == "java":
            command = JavaCommand()
        if language == "java_proxy":
            command = JavaCommandProxy()
        if language == "python":
            command = PythonCommand()
        if language == "node":
            command = NodeCommandAdapter()
        return command
