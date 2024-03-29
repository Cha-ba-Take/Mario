# -*- coding: UTF-8 -*-

from ActionGame.Character.characterMove import characterMove


class Move(characterMove):
    def __init__(self, goomba):
        super(Move, self).__init__(goomba)

        self.goomba = goomba
        self.direction = -1

        self.verticalPhysicalData = self.goomba.constants["verticalPhysicalData"]

    def walk(self):
        print(self.direction)
        self.horizontalVelocity = self.horizontalVelocityLimit * self.direction

    def moveX(self):
        state = self.character.event.getState()

        if state == 2:
            if self.goomba.isCollide == 5:
                self.direction = -1
            elif self.goomba.isCollide == 6:
                self.direction = 1
            self.walk()

        self.character.x += self.horizontalVelocity

        if self.goomba.gameManager.player.x == 512:
            if self.direction == -1:
                self.character.x -= self.goomba.gameManager.player.move.horizontalVelocity
            else:
                self.character.x -= self.goomba.gameManager.player.move.horizontalVelocity

    def moveY(self):
        self.fall()
        self.goomba.y += self.verticalVelocity
