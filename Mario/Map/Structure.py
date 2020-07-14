# -*- coding: UTF-8 -*-

import pygame


class Structure(pygame.sprite.Sprite):
    def __init__(self, map, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.map = map
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
