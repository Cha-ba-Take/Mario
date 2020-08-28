# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *


class Event:
    def __init__(self, goomba):
        self.goomba = goomba

        self.state = 0

    def stateMachine(self):
        isGround = self.goomba.isGround
        self.state = 2

    def defineState(self):
        self.stateMachine()

    def getState(self):
        return self.state
