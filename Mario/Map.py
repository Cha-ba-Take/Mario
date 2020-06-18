# -*- coding: UTF-8 -*-

import csv
import pygame

import System


def loadMapData(mapName):
    # マップデータの読み込み
    with open("data/" + mapName) as f:
        reader = csv.reader(f)
        mapData = [row for row in reader]
    return mapData


class Map:
    # マップクラス
    def __init__(self, screen, mapName):
        self.screen = screen
        self.chipSize = 64
        self.chipList = self.loadChip()
        self.mapData = loadMapData(mapName)
        self.map = self.make()
        self.x = 0
        self.previousX = 0

    def loadChip(self):
        # マップチップ画像の読み込み
        chipImage = System.loadImage("chips.png")
        return System.splitImage(chipImage, (self.chipSize, self.chipSize))

    def make(self):
        # マップの作成
        surface = pygame.Surface((1088, 960))
        for y in range(15):
            for x in range(17):
                chip = self.chipList[int(self.mapData[y][x])]
                position = (x * self.chipSize, y * self.chipSize)
                surface.blit(chip, position)
        return surface

    def update(self, marioX, marioVelocity):
        # マップの更新
        self.previousX = self.x

        if marioVelocity != 0:
            if marioX == 512:
                self.x += marioVelocity

        if self.previousX % 64 <= self.x % 64:
            return

        self.map.scroll(-64, 0)

        mapX = int(self.x // 64) + 17
        for y in range(15):
            chip = self.chipList[int(self.mapData[y][mapX])]
            position = (mapX * self.chipSize, y * self.chipSize)
            self.map.blit(chip, position)

    def draw(self):
        # マップの描画
        self.screen.blit(self.map, (-(self.x % 64), 0))
