from .command import Command
from .java_command import JavaCommand
from datetime import datetime
from ..exception.command_exception import CommandException


class JavaCommandProxy(Command):
    def __init__(self):
        self.name = "java_proxy"
        self.cmd = JavaCommand()

    def build(self, parameter):
        now = datetime.now()
        if now.hour < 17:
            command = self.cmd.build(parameter)
            return command
        raise CommandException("No permission", "458", "LATAM-02-wr545")
