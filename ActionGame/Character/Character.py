# -*- coding: UTF-8 -*-

import json

import pygame
from pygame.locals import *

import Image
from .Move import Move
from .Animation import Animation


class Character(pygame.sprite.Sprite):
    def __init__(self, gameManager, jsonFilePath):
        self.gameManager = gameManager

        self.constants = self.loadJson(jsonFilePath)

        self.imageData = self.constants["imageData"]
        self.images = self.getImage()
        self.image = self.images[0]

        self.collideChip = pygame.Surface((64, 64))
        self.collideChip.fill(Color("#FF0000"))

        self.initialPositionData = self.constants["initialPositionData"]
        self.x = self.initialPositionData["x"]
        self.y = self.initialPositionData["y"]
        self.rect = self.image.get_rect(left=self.x, top=self.y)

        self.isCollide = 0

        self.move = Move(self)
        self.animation = Animation(self)

    def loadJson(self, path):
        file = open(path, "r")

        return json.load(file)

    def getImage(self):
        baseImage = Image.loadImage(self.imageData["path"])
        imageList = Image.splitImage(baseImage, self.imageData["length"])

        return Image.flipImage(imageList)

    def getAtColor(self, position, color):
        try:
            if self.gameManager.collideSurface.get_at(position[0]) == Color(color):
                return True
            elif self.gameManager.collideSurface.get_at(position[1]) == Color(color):
                return True
        except IndexError:
            return False
        return False

    def collide(self, xCorrection=0):
        horizontalVelocity = int(self.move.horizontalVelocity)
        verticalVelocity = int(self.move.verticalVelocity)

        top = ((self.x, self.rect.top - 4), (self.x + self.rect.w, self.rect.top - 4))
        bottom = ((self.rect.left, self.rect.bottom + verticalVelocity + 4), (self.rect.right, self.rect.bottom + verticalVelocity + 4))
        left = ((self.rect.left - 4, self.rect.top + 4), (self.rect.left - 4, self.rect.bottom - 4))
        right = ((self.rect.right + 4, self.rect.top + 4), (self.rect.right + 4, self.rect.bottom - 4))

        self.isCollide = 0

        if self.getAtColor(right, "#FFFFFF"):
            self.isCollide += 1
        if self.getAtColor(left, "#FFFFFF"):
            self.isCollide += 2
        if self.getAtColor(bottom, "#FFFFFF"):
            self.isCollide += 4

    def update(self):
        self.collide()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]

    def draw(self):
        self.gameManager.collideSurface.blit(self.collideChip, (self.x, self.y))
        self.gameManager.screen.blit(self.image, (self.x, self.y))
