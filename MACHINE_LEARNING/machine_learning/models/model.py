from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def start(self):
        pass
