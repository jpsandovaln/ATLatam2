from .command import Command


class PythonCommand(Command):
    def __init__(self):
        self.name = "python"

    def build(self, parameter):
        PYTHON_COMPILER = parameter.get_binary_path() + 'python '
        command = PYTHON_COMPILER + ' ' + parameter.get_file_path()
        return command
