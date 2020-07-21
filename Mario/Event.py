# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import sys


def quitEvent():
    # 閉じるボタンが押された時の処理
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()


class Event:
    def __init__(self):
        self.keyEvent = 0
        self.previousKeyEvent = 0
        self.state = 0
        self.previousState = 0
        self.is_jump = {
            "first": False,
            "jumping": False
        }

    def keyEventGet(self):
        # キーが押されているかを取得
        keyPressed = pygame.key.get_pressed()
        self.previousKeyEvent = self.keyEvent
        self.keyEvent = 0
        keys = [K_RIGHT, K_LEFT, K_SPACE]
        for i in range(len(keys)):
            if keyPressed[keys[i]]:
                self.keyEvent += 2 ** i

    def stateMachine(self):
        # ステートマシン
        if self.keyEvent == 0:
            self.state = 0
        elif self.keyEvent == 1:
            self.state = 1
        elif self.keyEvent == 2:
            self.state = 2
        elif self.keyEvent == 4:
            self.state = 4
            if self.previousKeyEvent == 0 and self.is_jump["jumping"] is False:
                self.is_jump["jumping"] = True

