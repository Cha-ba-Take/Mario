# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *

class ScrollSystem:
    def __init__(self, gameManager):
        self.gameManager = gameManager

        self.worldX = 0
        self.previousWorldX = 0

    def update(self):
        self.previousWorldX = self.worldX

        if self.gameManager.player.move.horizontalVelocity > 0:
            if self.gameManager.player.x == 512:
                self.worldX += self.gameManager.player.move.horizontalVelocity

        if self.previousWorldX % 512 <= self.worldX % 512:
            return

        self.gameManager.scrollSurface.scroll(-512, 0)

    def draw(self):
        self.gameManager.screen.blit(self.gameManager.scrollSurface, (-(self.worldX % 512), 0))
