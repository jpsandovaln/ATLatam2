import os
from ..exception.parameter_exception import ParameterException
from ..validator.empty_or_none_validator import EmptyOrNoneValidator
from ..validator.file_validator import FileValidator
from ..validator.context import Context


class Parameter:
    def __init__(self, file_path: str, folder_path: str, binary_path: str):
        self._file_path = file_path
        self._folder_path = folder_path
        self._binary_path = binary_path

    def get_file_path(self) -> str:
        return self._file_path

    def get_folder_path(self) -> str:
        return self._folder_path

    def get_binary_path(self) -> str:
        return self._binary_path

    def validate(self) -> None:
        strategies: list = [
            EmptyOrNoneValidator("filepath", self._file_path),
            EmptyOrNoneValidator("folderPath", self._folder_path),
            EmptyOrNoneValidator("binaryPath", self._binary_path),
            FileValidator(self._file_path, True),
            FileValidator(self._folder_path, False)
        ]
        context = Context(strategies)
        context.validate()
