# -*- Coding: UTF-8 -*-

import pygame
from pygame.locals import *
import sys

from Character.Player.Player import Player
from Character.Enemy.EnemyFactory import EnemyFactory


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        self.player = Player(self)
        self.enemyFactory = EnemyFactory(self)

        self.frame = 0
        self.clock = pygame.time.Clock()

    def process(self):
        self.quit()

        self.update()
        self.draw()

        self.frame += 1

        self.clock.tick(60)

    def quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    def update(self):
        if self.frame % 45 == 0:
            self.enemyFactory.make("Goomba")
        self.enemyFactory.update()
        self.player.update()

    def draw(self):
        self.screen.fill(Color("#AAAAAA"))

        self.enemyFactory.draw()
        self.player.draw()

        pygame.display.update()
