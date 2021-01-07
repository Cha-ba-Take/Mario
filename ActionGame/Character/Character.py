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

        self.isGround = True

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

    def judgmentIsGround(self, xCorrection=0):
        leftX = int(self.x + xCorrection)
        rightX = int(self.x + self.rect.w - xCorrection - 1)
        y = int(self.rect.y + self.rect.h + self.move.verticalVelocity)
        if self.rect.y < 832:
            if 0 <= self.rect.x <= 1088:
                if self.getAtColor(leftX, y, "#FFFFFF"):
                    self.isGround = True
                elif self.getAtColor(rightX, y, "#FFFFFF"):
                    self.isGround = True
                else:
                    self.isGround = False
            else:
                self.isGround = True

        # -> デバッグ用
        elif self.rect.y == 896:
            self.isGround = True
        else:
            self.isGround = False
        # <-

    def update(self):
        self.judgmentIsGround()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]

    def draw(self):
        self.gameManager.collideSurface.blit(self.collideChip, (self.x, self.y))
        self.gameManager.screen.blit(self.image, (self.x, self.y))
