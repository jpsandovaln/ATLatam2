from .command import Command
from .java_command import JavaCommand
from datetime import datetime


class CommandProxy(Command):
    def __init__(self, command):
        self.name = "java_proxy"
        self.cmd : Command = command

    def build(self, parameter):
        now = datetime.now()
        if now.hour > 17:
            command = self.cmd.build(parameter)
            return command
        raise Exception("No permission")
