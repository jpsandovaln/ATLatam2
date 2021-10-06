from .command import Command
from ..exception.command_exception import CommandException
from .parameter import Parameter



class JavaCommand(Command):

    def __init__(self):
        self.name = "java"

    def build(self, parameter):
        if parameter is None or not isinstance(parameter, Parameter):
            raise CommandException("input invalid", "400", "Latam-02-654")
        parameter.validate()
        JAVA_COMPILER = parameter.get_binary_path() + 'javac '
        JAVA_EXECUTE = parameter.get_binary_path() + 'java '
        JAVA_CP_PARAM = '-cp '
        JAVA_AND = ' && '

        command = JAVA_COMPILER + parameter.get_file_path() + JAVA_AND + JAVA_EXECUTE + JAVA_CP_PARAM + parameter.get_folder_path() + 'EjemploJava8'
        return command
