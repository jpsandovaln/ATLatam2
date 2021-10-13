import abc


class IDocState(abc.ABC):
    @abc.abstractmethod
    def display_state(self) -> str:
        """Implement display state method"""
