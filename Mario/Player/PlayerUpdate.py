# -*- coding: UTF-8 -*-

from Player.Move import MoveX
from Player.Move import MoveY

from Player.Animation import Animation


class PlayerUpdate:
    def __init__(self, player):
        self.player = player
        self.event = self.player.event
        self.marioX = self.player.display.marioX
        self.marioY = self.player.display.marioY

    def update(self):
        # プレイヤーの更新
        self.event.stateMachine()

        self.getDirection()
        self.move()
        Animation.Animation(self.player).playerAnimation()

    def getDirection(self):
        if self.event.keyEvent == 1:
            self.player.direction = True
        elif self.event.keyEvent == 2:
            self.player.direction = False

    def move(self):
        # プレイヤーの移動
        MoveX.MoveX(self.player).move()
        MoveY.MoveY(self.player).move()
        self.player.rect = self.player.image.get_rect(topleft=(self.marioX, self.marioY))
