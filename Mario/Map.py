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
        # マップの更新
        self.previousWorldX = self.worldX

        if self.display.velocityX > 0:
            if self.display.marioX == 512:
                self.worldX += self.display.velocityX

        if self.previousWorldX % 64 <= self.worldX % 64:
            return

        self.map.scroll(-64, 0)

        mapX = int(self.worldX // 64) + 17
        for y in range(15):
            chip = self.chipList[int(self.mapData[y][mapX])]
            position = (mapX * self.chipSize[0], y * self.chipSize[1])
            self.map.blit(chip, position)

    def draw(self):
        # マップの描画
        self.display.screen.blit(self.map, (-(self.worldX % 64), 0))
