class Node:
    def __init__(self, file):
        self.__file = file

    def create_command(self):
        return f"node {self.__file}"
