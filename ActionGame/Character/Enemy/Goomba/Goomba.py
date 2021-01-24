# -*- coding: UTF-8 -*-

from Character.Character import Character
from .Event import Event
from .Move import Move
from .Animation import Animation

from pygame.locals import *


class Goomba(Character):
    def __init__(self, gameManager):
        super(Goomba, self).__init__(gameManager, "Character\Enemy\Goomba\Data\Constants.json")

        self.initialPositionData = None

        self.event = Event(self)
        self.move = Move(self)
        self.animation = Animation(self)

    def collide(self, xCorrection=0):
        horizontalVelocity = int(self.move.horizontalVelocity)
        verticalVelocity = int(self.move.verticalVelocity)

        top = ((self.x, self.rect.top - 4), (self.x + self.rect.w, self.rect.top - 4))
        bottom = ((self.rect.left, self.rect.bottom + verticalVelocity + 4), (self.rect.right, self.rect.bottom + verticalVelocity + 4))
        left = ((self.rect.left - 4, self.rect.top + 4), (self.rect.left - 4, self.rect.bottom - 4))
        right = ((self.rect.right + 4, self.rect.top + 4), (self.rect.right + 4, self.rect.bottom - 4))

        self.isCollide = 0

        if self.getAtColor(right, "#FFFFFF"):
            self.isCollide += 1
        if self.getAtColor(left, "#FFFFFF"):
            self.isCollide += 2
        if self.getAtColor(bottom, "#FFFFFF"):
            self.isCollide += 4

    def update(self):
        self.collide()
        print(self.isCollide)
        self.event.defineState()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]
