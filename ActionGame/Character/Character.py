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

    def getAtColor(self, x, y, color):
        if self.gameManager.collideSurface.get_at((x, y)) == Color(color):
            return True
        return False

    def collide(self, xCorrection=0):
        right = int(self.x + self.rect.w)
        left = int(self.x)
        top = int(self.y)
        bottom = int(self.y + self.rect.h)
        horizontalVelocity = int(self.move.horizontalVelocity)
        verticalVelocity = int(self.move.verticalVelocity)
        self.isCollide = 0
        if 0 <= left + horizontalVelocity and right + horizontalVelocity < 1088:
            if self.getAtColor(right + horizontalVelocity, top + 1, "#FFFFFF") or self.getAtColor(right + horizontalVelocity, bottom - 1, "#FFFFFF"):
                self.isCollide += 1
            if self.getAtColor(left + horizontalVelocity, top + 1, "#FFFFFF") or self.getAtColor(left + horizontalVelocity, bottom - 1, "#FFFFFF"):
                self.isCollide += 2
            if self.y < 832:
                if self.getAtColor(left, bottom + verticalVelocity, "#FFFFFF") or self.getAtColor(right, bottom + verticalVelocity, "#FFFFFF"):
                    self.isCollide += 4

    def update(self):
        self.collide()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]

    def draw(self):
        self.gameManager.collideSurface.blit(self.collideChip, (self.x, self.y))
        self.gameManager.screen.blit(self.image, (self.x, self.y))
