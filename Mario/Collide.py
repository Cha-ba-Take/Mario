# -*- coding: UTF-8 -*-

import pygame

ON_NOT_BLOCK_NUMBER = {1, 17, 18, 19, 20, 21, 22, 23, 31, 32}


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

    def getBlock(self, x, y):
        chip_number = int(self.display.map.mapData[y][x+1])
        print(f"chip_number(x+1): {chip_number}")
        for check_number in ON_NOT_BLOCK_NUMBER:
            if chip_number == check_number:
                return True

        return False
