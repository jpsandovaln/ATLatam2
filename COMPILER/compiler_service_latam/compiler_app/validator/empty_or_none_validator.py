from .validator_strategy import ValidatorStrategy
from ..exception.parameter_exception import ParameterException


class EmptyOrNoneValidator(ValidatorStrategy):
    def __init__(self, field, data):
        self.field = field
        self.data = data

    def validate(self):
        if self.data is None or str(self.data).strip() == "":
            message = "The field: " + self.field + " is invalid"
            raise ParameterException(message, "Latam-02-44875")
