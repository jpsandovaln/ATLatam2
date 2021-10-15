class Node:
    def __init__(self, file: str):
        self.__file = file

    def create_command(self) -> str:
        return f"node {self.__file}"
