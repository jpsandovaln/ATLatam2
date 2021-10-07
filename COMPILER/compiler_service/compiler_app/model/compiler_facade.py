from .command import Command
from .parameter import Parameter
from .execute import Execute
from .command_factory import CommandFactory


class CompilerFacade:
    def __init__(self):
        pass

    @staticmethod
    def compile(language: str, file: str, folder: str, binary: str) -> str:
        parameter = Parameter(file, folder, binary)
        parameter.validate()
        command: Command = CommandFactory.get_instance(language)
        build_command = command.build(parameter)
        execute = Execute(build_command)
        return execute.run()
