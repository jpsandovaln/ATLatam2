import abc


class Command(abc.ABC):

    @abc.abstractmethod
    def build(self, parameter):
        """build method should be implemented"""