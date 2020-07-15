# -*- coding: UTF-8 -*-

import pygame

import Animator
import Image

from Player import PlayerUpdate

PLAYER_Y = 772


class Player(pygame.sprite.Sprite):
    def __init__(self, display):
        self.display = display

        pygame.sprite.Sprite.__init__(self)

        self.playerImage = Image.Image("mario.png", True)
        baseImage = self.playerImage.load()
        self.images = self.playerImage.makePlayerImage(baseImage, (64, 64))
        self.image = self.images[0]

        self.animator = Animator.Animator(self.images)

        self.rect = self.image.get_rect(topleft=(self.display.marioX, PLAYER_Y))

        self.state = 0
        self.previousState = 0

    def update(self, event):
        PlayerUpdate.update(self).update(event)

    def draw(self):
        # プレイヤーの描画
        self.display.screen.blit(self.image, self.rect)
