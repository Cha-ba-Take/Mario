# -*- coding: UTF-8 -*-

from abc import ABC

from Player.Move import Move


class MoveX(Move.Move, ABC):
    def __init__(self, player):
        super().__init__(player)
        self.player = player
        self.state = self.player.event.state

    def move(self):
        # X軸方向の移動
        self.getVelocity()
        self.player.display.marioX += self.player.display.velocityX
        self.player.display.marioX = min(max(self.player.display.marioX, 0), 512)

    def getVelocity(self):
        # X軸方向の速度を取得
        if self.state == 0:
            self.player.display.velocityX = 0
        elif self.state == 1 or self.state == 3:
            if self.player.direction:
                self.player.display.velocityX = 4
            else:
                self.player.display.velocityX = -4
