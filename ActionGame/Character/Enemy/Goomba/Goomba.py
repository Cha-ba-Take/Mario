# -*- coding: UTF-8 -*-

from Character.Character import Character
from .Event import Event
from .Move import Move
from .Animation import Animation


class Goomba(Character):
    def __init__(self, gameManager):
        super(Goomba, self).__init__(gameManager, "ActionGame\Character\Enemy\Goomba\Data\Constants.json")

        self.event = Event(self)
        self.move = Move(self)
        self.animation = Animation(self)

    def update(self):
        self.judgmentIsGround()
        self.event.defineState()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]
