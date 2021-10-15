import abc


class Execute(abc.ABC):
    def run(self, cmd: str):
        """Implement run method"""
