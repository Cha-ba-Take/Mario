# -*- coding: UTF-8 -*-

from ActionGame.Character.characterAnimation import characterAnimation

class Animation(characterAnimation):
    def __init__(self, goomba):
        super(Animation, self).__init__(goomba)

        self.goomba = goomba

    def getState(self):
        state = self.goomba.event.getState()

        if state == 2:
            self.state = self.data["walk"]
