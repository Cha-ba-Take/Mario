# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *


class Event:
    def __init__(self, player):
        self.player = player

        self.keyEvent = 0
        self.previousKeyEvent = 0

        self.state = 0

    def defineKeyEvent(self):
        keyPressed = pygame.key.get_pressed()

        self.previousKeyEvent = self.keyEvent
        self.keyEvent = 0

        keys = [K_RIGHT, K_LEFT, K_SPACE]

        for i in range(len(keys)):
            if keyPressed[keys[i]]:
                self.keyEvent += 2 ** i

    def stateMachine(self):
        isGround = self.player.isGround

        if self.keyEvent == 1:
            self.state = 1
        elif self.keyEvent == 2:
            self.state = 2
        elif self.keyEvent == 4:
            if self.previousKeyEvent == 0:
                if self.player.isJump["jumping"] is False and isGround:
                    self.player.isJump["init"] = True
        elif self.keyEvent == 5:
            self.state = 1
            if self.previousKeyEvent == 1:
                if self.player.isJump["jumping"] is False and isGround:
                    self.player.isJump["init"] = True
        elif self.keyEvent == 6:
            self.state = 2
            if self.previousKeyEvent == 2:
                if self.player.isJump["jumping"] is False and isGround:
                    self.player.isJump["init"] = True
        else:
            self.state = 0

    def defineState(self):
        self.defineKeyEvent()
        self.stateMachine()

    def getState(self):
        return self.state

    def getKeyEvent(self):
        return self.keyEvent
