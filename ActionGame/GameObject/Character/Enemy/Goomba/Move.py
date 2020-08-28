# -*- coding: UTF-8 -*-

from ActionGame.GameObject.Character.Move import Move as characterMove


class Move(characterMove):
    def __init__(self, goomba):
        super(Move, self).__init__(goomba)

        self.goomba = goomba

        self.verticalPhysicalData = self.goomba.constants["verticalPhysicalData"]

    def moveX(self):
        state = self.character.event.getState()

        if state == 2:
            if self.horizontalVelocity > 0:
                self.stop()
            else:
                self.direction = -1
                self.walk()

        self.character.x += self.horizontalVelocity
        self.character.x = min(self.character.x, 736)

    def moveY(self):
        self.fall()

        self.goomba.y += self.verticalVelocity
        self.goomba.y = min(self.goomba.y, 536)
