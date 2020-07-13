from abc import ABCMeta, abstractmethod


class Move(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, player):
        """

        :player PlayerClass:
        """
        pass

    @abstractmethod
    def move(self): pass

    @abstractmethod
    def getVelocity(self): pass
