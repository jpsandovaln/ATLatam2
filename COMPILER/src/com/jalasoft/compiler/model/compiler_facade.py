from src.com.jalasoft.compiler.model.parameter import Parameter
from src.com.jalasoft.compiler.model.execute import Execute
from src.com.jalasoft.compiler.model.command_factory import CommandFactory


class CompilerFacade:
    def __init__(self):
        pass

    @staticmethod
    def compile(language, file, folder, binary):
        parameter = Parameter(file, folder, binary)
        command = CommandFactory.get_instance(language)
        build_command = command.build(parameter)
        execute = Execute(build_command)
        return execute.run()
