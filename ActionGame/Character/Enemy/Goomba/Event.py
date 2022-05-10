# -*- coding: UTF-8 -*-

class Event:
    def __init__(self, goomba):
        self.goomba = goomba

        self.state = 0

    def stateMachine(self):
        self.state = 2

    def defineState(self):
        self.stateMachine()

    def getState(self):
        return self.state
