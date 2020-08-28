# -*- coding: UTF-8 -*-

from .Goomba.Goomba import Goomba

class EnemyFactory:
    def __init__(self, gameManager):
        self.gameManager = gameManager
        self.enemyList = []

    def make(self, name):
        if name == "Goomba":
            self.enemyList.append(Goomba(self.gameManager))

    def update(self):
        for enemy in self.enemyList:
            enemy.update()

        for i in range(len(self.enemyList)):
            if self.enemyList[i].x < -64:
                self.enemyList.pop(i)
                break

    def draw(self):
        for enemy in self.enemyList:
            enemy.draw()