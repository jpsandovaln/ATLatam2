import subprocess
from ..exception.execute_exception import ExecuteException


class Execute:
    def __init__(self, cmd: str):
        self._cmd = cmd

    def run(self):
        try:
            result = subprocess.check_output(self._cmd, shell=True)
        except Execute as error:
            raise ExecuteException(error)
        return result
