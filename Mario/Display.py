# -*- coding: UTF-8 -*-

import pygame

from Map import MapListener
from Player import Player
import Collide


class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 960))
        pygame.display.set_caption("test")

        self.collide = Collide.Collide(self)

        self.map = MapListener.Map(self)

        self.marioX = 160
        self.world_marioX = self.marioX
        self.velocityX = 0
        self.marioY = 772
        self.velocityY = 0

        self.player = Player.Player(self)

        self.frame = 0

    def update(self, event):
        # 画面の更新
        self.map.update()
        self.player.update(event)

        self.frame += 1

    def draw(self):
        # 画面の描画
        self.map.draw()
        self.player.draw()

        pygame.display.update()
