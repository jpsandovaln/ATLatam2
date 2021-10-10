import os
from .validator_strategy import ValidatorStrategy
from ..exception.parameter_exception import ParameterException


class FileValidator(ValidatorStrategy):

    def __init__(self, data, isFile):
        self.data = data
        self.isFile = isFile

    def validate(self):
        if self.isFile:
            isFile = os.path.isfile(self.data)
            if not isFile:
                raise ParameterException("invalid file path", "Latam-02-4478578")
        else:
            isFolder = os.path.isdir(self.data)
            if not isFolder:
                raise ParameterException("invalid folder path", "Latam-02-44575")
