# -*- coding: UTF-8 -*-

import pygame

import Animator
import Image


class Player(pygame.sprite.Sprite):
    def __init__(self, display):
        self.display = display

        pygame.sprite.Sprite.__init__(self)

        self.playerImage = Image.Image("mario.png", True)
        baseImage = self.playerImage.load()
        self.images = self.playerImage.makePlayerImage(baseImage, (64, 64))
        self.image = self.images[0]

        self.animator = Animator.Animator(self.images)
        self.animationData = None

        self.y = 772
        self.rect = self.image.get_rect(topleft=(self.display.marioX, self.y))

        self.state = 0
        self.previousState = 0

        self.velocityY = 0

    def update(self, event):
        # プレイヤーの更新
        event.stateMachine()
        self.state = event.state
        self.previousState = event.previousState

        self.move()
        self.animation()

    def move(self):
        # プレイヤーの移動
        self.moveX()
        self.moveY()
        self.rect = self.image.get_rect(topleft=(self.display.marioX, self.y))

    def moveX(self):
        # X軸方向の移動
        self.getVelocityX()
        self.display.marioX += self.display.velocityX
        self.display.marioX = min(max(self.display.marioX, 0), 512)

    def moveY(self):
        # Y軸方向の移動
        self.getVelocityY()

    def getVelocityX(self):
        # X軸方向の速度を取得
        if self.state == 0:
            self.display.velocityX = 0
        elif self.state == 1:
            self.display.velocityX = 4
        elif self.state == 2:
            self.display.velocityX = -4

    def getVelocityY(self):
        # Y軸方向の速度を取得
        if self.state == 0:
            self.velocityY = 0

    def animation(self):
        # プレイヤーのアニメーション
        self.image = self.animator.getImage(self.display.frame, self.getAnimationData())

    def getAnimationData(self):
        # プレイヤーのアニメーションデータを取得
        if self.state == 0:
            self.animationData = [1, 0, None]
        elif self.state == 1:
            self.animationData = [3, 1, 4]
        elif self.state == 2:
            self.animationData = [3, 7, 4]
        return self.animationData

    def draw(self):
        #プレイヤーの描画
        self.display.screen.blit(self.image, self.rect)
