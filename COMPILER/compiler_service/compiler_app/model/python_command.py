from .command import Command
from .parameter import Parameter


class PythonCommand(Command):
    def __init__(self):
        self.name = "python"

    def build(self, parameter: Parameter) -> str:
        PYTHON_COMPILER: str = parameter.get_binary_path() + 'python '
        command: str = PYTHON_COMPILER + ' ' + parameter.get_file_path()
        return command
