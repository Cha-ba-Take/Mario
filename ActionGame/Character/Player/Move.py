# -*- coding: UTF-8 -*-

from Character.Move import Move as characterMove


class Move(characterMove):
    def __init__(self, player):
        super(Move, self).__init__(player)

        self.player = player

        self.verticalPhysicalData = self.player.constants["verticalPhysicalData"]
        self.riseInitialVelocity = self.verticalPhysicalData["riseInitialVelocity"]
        self.riseAcceleration = self.verticalPhysicalData["riseAcceleration"]

    def moveY(self):
        if self.player.isJump["init"] or self.player.isJump["rise"]:
            self.jump()
            self.player.isJump["jumping"] = True
        else:
            self.fall()

        self.player.y += self.verticalVelocity
        self.player.y = min(self.player.y, 896)

        if self.player.isCollide in (4, 5, 6):
            self.player.isJump["jumping"] = False

    def jump(self):
        if self.player.isJump["init"]:
            self.verticalVelocity = self.riseInitialVelocity
            self.player.isJump["init"] = False
            self.player.isJump["rise"] = True
            return

        if self.player.event.getKeyEvent() in (4, 5, 6):
            self.verticalVelocity += self.riseAcceleration
            if self.verticalVelocity >= 0:
                self.verticalVelocity = 0
                self.player.isJump["rise"] = False
        else:
            self.player.isJump["rise"] = False

    def isSlip(self):
        if self.horizontalVelocity > 0:
            return 1
        elif self.horizontalVelocity < 0:
            return 2
        else:
            return 0
