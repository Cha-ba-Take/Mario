# -*- coding: UTF-8 -*-

from abc import ABC

from Player.Move import Move


class MoveX(Move.Move, ABC):
    def __init__(self, player, event):
        self.player = player
        self.event = event
        self.state = self.player.state

        self.marioX = 0
        self.marioY = 0
        self.is_collide = False

    def move(self):
        self.marioX = int(self.player.display.world_marioX // 64)
        self.marioY = int(self.player.display.marioY // 64)

        self.is_collide = self.player.display.collide.getBlock(self.marioX, self.marioY)

        # X軸方向の移動
        self.getVelocity()
        if self.player.display.collide.onBlocks(self.player.rect):
            self.player.display.velocityX = 0

        self.player.display.marioX += self.player.display.velocityX
        self.player.display.marioX = min(max(self.player.display.marioX, -4), 512)

        if self.player.display.marioX > 0:
            self.player.display.world_marioX += self.player.display.velocityX

    def getVelocity(self):
        # X軸方向の速度を取得
        if self.state == 0:
            self.player.display.velocityX = 0
        elif self.state == 1:
            if self.event.is_jump["jumping"] is False:
                self.player.display.velocityX = 4
                if self.is_collide is True:
                    self.player.display.velocityX = 0
        elif self.state == 2:
            if self.event.is_jump["jumping"] is False:
                self.player.display.velocityX = -4
