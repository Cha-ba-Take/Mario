# -*- coding: UTF-8 -*-

from Character.Move import Move as characterMove


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

        if self.goomba.gameManager.player.x == 512:
            self.character.x -= self.goomba.gameManager.player.move.horizontalVelocity

    def moveY(self):
        self.fall()

        self.goomba.y += self.verticalVelocity
