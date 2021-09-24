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
