# -*- coding: UTF-8 -*-

import pygame

import System


class Player(pygame.sprite.Sprite):
    moveVelocity = 6
    dashVelocity = 8

    frame = 0
    moveAnimationCycle = 6
    dashAnimationCycle = 4

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        images = System.loadImage("mario.png", True)
        self.images = System.splitImage(images, (64, 64), True)
        self.image = self.images[0]
        self.x = 160
        self.y = 772
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.velocity = 0
        self.state = 0

    def update(self, state):
        self.state = state

        if self.state == 0:
            self.velocity = 0
        elif self.state == 1:
            self.velocity = 0
        elif self.state == 2:
            self.velocity = self.moveVelocity
        elif self.state == 3:
            self.velocity = -self.moveVelocity
        elif self.state == 4:
            self.velocity = self.dashVelocity
        elif self.state == 5:
            self.velocity = -self.dashVelocity

        self.x += self.velocity
        if self.x > 512:
            self.x = 512
        if self.x < 0:
            self.x = 0

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.frame += 1
        animation = [
            0,
            6,
            int(self.frame / self.moveAnimationCycle % 3) + 1,
            int(self.frame / self.moveAnimationCycle % 3) + 7,
            int(self.frame / self.dashAnimationCycle % 3) + 1,
            int(self.frame / self.dashAnimationCycle % 3) + 7,
        ]

        self.image = self.images[animation[self.state]]

        return self.state

    def draw(self):
        self.screen.blit(self.image, self.rect)
