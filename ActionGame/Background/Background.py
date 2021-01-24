# -*- coding: UTF-8 -*-

import csv
import pygame
from pygame.locals import *

import Image


def loadMapData(mapName):
    with open("Background/data/" + mapName) as f:
        reader = csv.reader(f)
        mapData = [row for row in reader]
    return mapData


class Background:
    def __init__(self, gameManager):
        self.gameManager = gameManager
        self.images = self.getImage()

        self.backgroundData = loadMapData("course1-1.csv")

        self.collideSurface = pygame.Surface((1088, 960))

        self.surface = pygame.Surface((1088, 960))
        self.make()

        self.worldX = 0
        self.previousWorldX = 0

    def getImage(self):
        baseImage = Image.loadImage("Background/Data/chips.png")
        imageLength = baseImage.get_width()
        imageSplitLength = int(imageLength / 64)
        return Image.splitImage(baseImage, imageSplitLength)

    def make(self):
        for y in range(15):
            for x in range(17):
                self.surfaceDraw(x, y, True)

    def surfaceDraw(self, x, y, special=False):
        index = int(self.backgroundData[y][x])
        if index < 33:
            chip = self.images[index]
        else:
            chip = self.images[0]
        collideChip = pygame.Surface((64, 64))

        if special:
            position = (x * 64, y * 64)
        else:
            position = (1024, y * 64)

        if index in (1, 17, 18, 19, 20, 21, 31, 32):
            collideChip.fill(Color("#FFFFFF"))
        elif index == 33:
            self.gameManager.enemyFactory.make("Goomba")
            self.gameManager.enemyFactory.enemyList[-1].x = 1024 + 16
            self.gameManager.enemyFactory.enemyList[-1].y = y * 64 - 4
        else:
            collideChip.fill(Color("#000000"))

        self.collideSurface.blit(collideChip, position)
        self.surface.blit(chip, position)

    def update(self):
        self.previousWorldX = self.worldX

        if self.gameManager.player.x == 512:
            self.worldX += self.gameManager.player.move.horizontalVelocity

        if self.previousWorldX % 64 <= self.worldX % 64:
            return

        self.surface.scroll(-64, 0)
        self.collideSurface.scroll(-64, 0)

        mapX = int(self.worldX // 64) + 16
        for y in range(15):
            self.surfaceDraw(mapX, y)

    def draw(self):
        self.gameManager.collideSurface.blit(self.collideSurface, (-(self.worldX % 64), 0))
        self.gameManager.screen.blit(self.surface, (-(self.worldX % 64), 0))
