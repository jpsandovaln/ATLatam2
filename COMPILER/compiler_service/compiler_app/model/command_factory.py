from .java_command import JavaCommand
from .java_command_proxy import JavaCommandProxy
from .python_command import PythonCommand
from .node_command_adapter import NodeCommandAdapter
from ..exception.command_exception import CommandException



class CommandFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_instance(language):
        if language == "java":
            return JavaCommand()
        if language == "java_proxy":
            return JavaCommandProxy()
        if language == "python":
            return PythonCommand()
        if language == "node":
            return NodeCommandAdapter()
        raise CommandException("Language not supported", "401", "Latam-02-8755")
