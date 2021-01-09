# -*- Coding: UTF-8 -*-

import pygame
from pygame.locals import *
import sys

from Background.Background import Background
from Character.Player.Player import Player
from Character.Enemy.EnemyFactory import EnemyFactory
from ScrollSystem import ScrollSystem

screenMagnification = 4
screenWidth = 256 * screenMagnification
screenHeight = 240 * screenMagnification
screenSize = (screenWidth, screenHeight)
collideSurfaceSize = (screenWidth + 64, screenHeight)


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screenSize)
        self.collideSurface = pygame.Surface(collideSurfaceSize)

        self.background = Background(self)
        self.player = Player(self)
        self.enemyFactory = EnemyFactory(self)
        self.scrollSystem = ScrollSystem(self)

        self.frame = 0
        self.clock = pygame.time.Clock()

    def process(self):
        self.gameQuit()

        self.update()
        self.draw()

        self.frame += 1

        self.clock.tick(60)

    def gameQuit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.background.update()

        self.enemyFactory.update()

        self.player.update()

        for i in range(len(self.enemyFactory.enemyList)):
            if self.player.rect.colliderect(self.enemyFactory.enemyList[i].rect):
                self.enemyFactory.enemyList.pop(i)
                break

    def draw(self):
        self.collideSurface.fill((0, 0, 0))
        self.background.draw()
        self.enemyFactory.draw()
        self.player.draw()
        # self.screen.blit(self.collideSurface, (0, 0))

        pygame.display.update()
