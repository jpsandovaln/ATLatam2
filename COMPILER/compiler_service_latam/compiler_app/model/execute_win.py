import subprocess

from .execute import Execute
from ..exception.execute_exception import ExecuteException


class ExecuteWin(Execute):
    def run(self, cmd):
        try:
            result = subprocess.check_output(cmd, shell=True)
            return result
        except Execute as error:
            raise ExecuteException(error)
