# -*- coding: UTF-8 -*-

from ..Animation import Animation as characterAnimation

class Animation(characterAnimation):
    def __init__(self, player):
        super(Animation, self).__init__(player)

        self.player = player

    def getState(self):
        state = self.player.event.getState()
        isSlip = self.player.move.isSlip()
        direction = self.player.move.getDirection()
        isJump = self.player.isJump

        if state == 1:
            if isSlip == 2:
                self.state = self.data["leftLookBack"]
            else:
                self.state = self.data["rightWalk"]
        elif state == 2:
            if isSlip == 1:
                self.state = self.data["rightLookBack"]
            else:
                self.state = self.data["leftWalk"]
        else:
            if direction == 1:
                if isSlip == 1:
                    self.state = self.data["rightSlip"]
                elif isSlip == 0:
                    self.state = self.data["rightIdle"]
            else:
                if isSlip == 2:
                    self.state = self.data["leftSlip"]
                elif isSlip == 0:
                    self.state = self.data["leftIdle"]

        if isJump["jumping"]:
            if direction == 1:
                self.state = self.data["rightJump"]
            else:
                self.state = self.data["leftJump"]
