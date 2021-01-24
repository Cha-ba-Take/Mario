# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *

from .Goomba.Goomba import Goomba

class EnemyFactory:
    def __init__(self, gameManager):
        self.gameManager = gameManager

        self.enemyList = []

        self.worldX = 0
        self.previousWorldX = 0

    def make(self, name):
        if name == "Goomba":
            self.enemyList.append(Goomba(self.gameManager))


    def update(self):
        for enemy in self.enemyList:
            enemy.update()
            enemy.rect = enemy.image.get_rect(left=enemy.x, top=enemy.y)

        for i in range(len(self.enemyList)):
            if self.enemyList[i].x < -64 or self.enemyList[i].y > 960:
                self.enemyList.pop(i)
                break


    def draw(self):
        for enemy in self.enemyList:
            enemy.draw()
