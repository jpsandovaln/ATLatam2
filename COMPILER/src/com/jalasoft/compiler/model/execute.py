import os


class Execute:
    def __init__(self, cmd):
        self._cmd = cmd

    def run(self):
        return os.system(self._cmd)
