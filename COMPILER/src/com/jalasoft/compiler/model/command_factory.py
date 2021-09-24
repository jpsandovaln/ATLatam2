from src.com.jalasoft.compiler.model.java_command import JavaCommand
from src.com.jalasoft.compiler.model.python_command import PythonCommand


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
