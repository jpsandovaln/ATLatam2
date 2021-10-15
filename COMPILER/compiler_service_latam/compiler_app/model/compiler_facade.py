from .command import Command
from .parameter import Parameter
from .execute import Execute
from .command_factory import CommandFactory


class CompilerFacade:
    def __init__(self):
        pass

    @staticmethod
    def compile(language: str, file: str, folder: str, binary: str, execute: Execute) -> str:
        parameter = Parameter(file, folder, binary)
        parameter.validate()
        command: Command = CommandFactory.get_instance(language)
        build_command = command.build(parameter)
        return execute.run(build_command)
