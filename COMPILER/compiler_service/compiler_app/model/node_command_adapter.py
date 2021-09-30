from .command import Command
from .node_cmd import Node


class NodeCommandAdapter(Command):
    def __init__(self):
        self.name = "node"

    def build(self, parameter):
        node = Node(parameter.get_file_path())
        result = node.create_command()
        return result
