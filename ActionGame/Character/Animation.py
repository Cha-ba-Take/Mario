# -*- coding: UTF-8 -*-

class Animation:
    def __init__(self, character):
        self.character = character

        self.data = self.character.constants["animationData"]

        self.state = None

    def getState(self):
        state = self.character.event.getState()
        isSlip = self.character.move.isSlip()
        direction = self.character.move.getDirection()
        isJump = self.character.isJump

        if state == 1:
            self.state = self.data["rightWalk"]
        elif state == 2:
            self.state = self.data["leftWalk"]

    def getIndex(self):
        self.getState()

        times = self.state[0]
        locate = self.state[1]
        animationCycle = self.state[2]

        frame = self.character.gameManager.frame

        index = locate if animationCycle is None else int(frame / animationCycle % times) + locate

        return index
