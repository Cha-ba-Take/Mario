# -*- coding: UTF-8 -*-

import os
import pygame
from pygame.locals import *


def loadImage(path, flag=False):
    # 画像を読み込む
    filePath = os.path.join("data/images", path)
    image = pygame.image.load(filePath)
    image.convert_alpha() if flag else image.convert()
    return image


def splitImage(image, chipSize, flag=False):
    # 連続した画像のデータを分割して、リストに入れる
    chipList = []
    chipBase = pygame.Surface((chipSize[0], chipSize[1]))
    for i in range(0, image.get_width(), chipSize[0]):
        chip = chipBase.copy()
        chip.blit(image, (-i, 0))
        if flag:
            chip.set_colorkey(Color("#FF00FF"), RLEACCEL)
            chip.convert()
        chipList.append(chip)
    return chipList
