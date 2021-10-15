from .command import Command
from .java_command import JavaCommand
from datetime import datetime

from .parameter import Parameter
from ..exception.command_exception import CommandException


class JavaCommandProxy(Command):
    def __init__(self):
        self.name = "java_proxy"
        self.cmd: JavaCommand = JavaCommand()

    def build(self, parameter: Parameter) -> str:
        now: datetime = datetime.now()
        if now.hour < 17:
            command: str= self.cmd.build(parameter)
            return command
        raise CommandException("No permission", "458", "LATAM-02-wr545")
