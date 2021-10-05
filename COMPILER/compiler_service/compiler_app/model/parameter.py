import os
from ..exception.parameter_exception import ParameterException


class Parameter:
    def __init__(self, file_path, folder_path, binary_path):
        self._file_path = file_path
        self._folder_path = folder_path
        self._binary_path = binary_path

    def get_file_path(self):
        return self._file_path

    def get_folder_path(self):
        return self._folder_path

    def get_binary_path(self):
        return self._binary_path

    def validate(self):
        if self._file_path is None or str(self._file_path).strip() == "":
            raise ParameterException("invalid file, the value is empty", "Latam-02-44875")
        isFile = os.path.isfile(self._file_path)
        if not isFile:
            raise ParameterException("invalid file path", "Latam-02-4478578")
        if self._binary_path is None or str(self._binary_path).strip() == "":
            raise ParameterException("invalid binary file, the value is empty", "Latam-02-44575")
        if self._folder_path is None or str(self._folder_path).strip() == "":
            raise ParameterException("invalid folder, the value is empty", "Latam-02-444534")
        isFolder = os.path.isdir(self._folder_path)
        if not isFolder:
            raise ParameterException("invalid folder path", "Latam-02-44575")
