# -*- coding: UTF-8 -*-

import pygame


class Collide:
    def __init__(self, display):
        self.display = display
        self.blocks = pygame.sprite.LayeredUpdates()

    def onBlocks(self, rect):
        for block in self.blocks:
            isCollide = block.rect.colliderect(rect)
            if isCollide:
                return True
            else:
                return False
