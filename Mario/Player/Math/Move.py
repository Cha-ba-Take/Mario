from abc import ABCMeta, abstractmethod


class Move(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, player):
        """

        :param PlayerClass:
        """
        pass

    @abstractmethod
    def move(self): pass

    @abstractmethod
    def getVelocity(self): pass
