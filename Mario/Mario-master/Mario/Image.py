# -*- coding: UTF-8 -*-

import os
import pygame
from pygame.locals import *


def flip(chipList):
    for i in range(len(chipList)):
        chipList.append(pygame.transform.flip(chipList[i], True, False))
    return chipList


class Image:
    def __init__(self, fileName, transparency=False):
        self.filePath = os.path.join("data/images", fileName)
        self.transparency = transparency

    def load(self):
        # 画像の読み込み
        image = pygame.image.load(self.filePath)
        image.convert_alpha() if self.transparency else image.convert()
        return image

    def split(self, image, chipSize):
        # 画像をチップに分割
        chipList = []
        chipBase = pygame.Surface((chipSize[0], chipSize[1]))
        for i in range(0, image.get_width(), chipSize[0]):
            chip = chipBase.copy()
            chip.blit(image, (-i, 0))
            if self.transparency:
                chip.set_colorkey(Color("#FF00FF"), RLEACCEL)
                chip.convert()
            chipList.append(chip)
        return chipList

    def makePlayerImage(self, image, chipSize):
        return flip(self.split(image, chipSize))
