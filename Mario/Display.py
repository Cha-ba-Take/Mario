# -*- coding: UTF-8 -*-

import pygame

import Map
import Player


class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 960))
        pygame.display.set_caption("test")

        self.map = Map.Map(self)

        self.marioX = 160
        self.velocityX = 0
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
