from .parameter import Parameter
from .execute import Execute
from .command_factory import CommandFactory


class CompilerFacade:
    def __init__(self):
        pass

    @staticmethod
    def compile(language, file, folder, binary) -> str:
        parameter = Parameter(file, folder, binary)
        parameter.validate()
        command = CommandFactory.get_instance(language)
        build_command = command.build(parameter)
        execute = Execute(build_command)
        return execute.run()
