# -*- coding: UTF-8 -*-

import csv
import pygame

import Image


def loadMapData(mapName):
    # マップデータの読み込み
    with open("data/" + mapName) as f:
        reader = csv.reader(f)
        mapData = [row for row in reader]
    return mapData


class Map:
    def __init__(self, display):
        self.display = display

        self.chipSize = (64, 64)
        mapImage = Image.Image("chips.png")
        baseChip = mapImage.load()
        self.chipList = mapImage.split(baseChip, self.chipSize)

        self.mapData = loadMapData("course1-1.csv")

        self.map = self.make()

        self.worldX = 0
        self.previousWorldX = 0

    def make(self):
        # マップの作成
        surface = pygame.Surface((1088, 960))
        for y in range(15):
            for x in range(17):
                chip = self.chipList[int(self.mapData[y][x])]
                position = (x * self.chipSize[0], y * self.chipSize[1])
                surface.blit(chip, position)
        return surface

    def update(self):
        self.previousWorldX = self.worldX
        MapUpdate(self)

    def draw(self):
        # マップの描画
        self.display.screen.blit(self.map, (-(self.worldX % 64), 0))

class MapUpdate():
    def __init__(self, Map):
        self.MapInstance = Map

        self.scroll()
        self.blit()

    def scroll(self):
        if self.checkScroll() is False:
            return

        self.MapInstance.map.scroll(-64, 0)

    def checkScroll(self):
        if self.MapInstance.display.marioX == 512:
            self.MapInstance.worldX += self.MapInstance.display.velocityX

        if self.MapInstance.previousWorldX % 64 <= self.MapInstance.worldX % 64: return False
        return True

    def blit(self):
        mapX = int(self.MapInstance.worldX // 64) + 17
        for y in range(15):
            chip = self.MapInstance.chipList[int(self.MapInstance.mapData[y][mapX])]
            position = (mapX * self.MapInstance.chipSize[0], y * self.MapInstance.chipSize[1])
            self.MapInstance.map.blit(chip, position)




