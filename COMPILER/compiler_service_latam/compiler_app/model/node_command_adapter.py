from .command import Command
from .node_cmd import Node
from .parameter import Parameter


class NodeCommandAdapter(Command):
    def __init__(self):
        self.name: str = "node"

    def build(self, parameter: Parameter) -> str:
        node: Node = Node(parameter.get_file_path())
        result: str = node.create_command()
        return result
