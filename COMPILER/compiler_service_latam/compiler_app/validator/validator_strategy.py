import abc


class ValidatorStrategy(abc.ABC):
    @abc.abstractmethod
    def validate(self):
        """validate method should be implemented"""
