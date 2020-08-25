# -*- coding: UTF-8 -*-

import json

import pygame

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

    def judgmentIsGround(self):
        if self.y == 536:
            self.isGround = True
        else:
            self.isGround = False

    def update(self):
        self.judgmentIsGround()
        self.move.move()
        self.image = self.images[self.animation.getIndex()]

    def draw(self):
        self.gameManager.screen.blit(self.image, (self.x, self.y))
