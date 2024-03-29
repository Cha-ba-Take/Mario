# -*- coding: UTF-8 -*-

import Event
import Move
import Animation

import sys
sys.path.append('../Character')

from ActionGame.Character import Character

from pygame.locals import *


class Player(Character):
    def __init__(self, gameManager):
        super(Player, self).__init__(gameManager, "Character\Player\Data\Constants.json")

        self.collideChip.fill(Color("#FFFF00"))

        self.isJump = {
            "init" : False,
            "rise" : False,
            "jumping" : False
        }

        self.event = Event.Event(self)
        self.move = Move.Move(self)
        self.animation = Animation.Animation(self)

    def update(self):
        self.collide(12)
        self.event.defineState()
        self.move.move()
        self.rect = self.image.get_rect(left=self.x, top=self.y)
        self.image = self.images[self.animation.getIndex()]
