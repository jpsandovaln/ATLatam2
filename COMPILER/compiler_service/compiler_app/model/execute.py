import subprocess


class Execute:
    def __init__(self, cmd):
        self._cmd = cmd

    def run(self):
        result = subprocess.check_output(self._cmd, shell=True)
        return result
