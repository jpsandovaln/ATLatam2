import abc
from .parameter import Parameter


class Command(abc.ABC):

    @abc.abstractmethod
    def build(self, parameter: Parameter) -> str:
        """build method should be implemented"""
