# -*- coding: UTF-8 -*-

from abc import ABC

from Player.Move import Move


class MoveY(Move.Move, ABC):
    def __init__(self, player):
        super().__init__(player)
        self.player = player

    def move(self):
        self.getVelocity()
        self.player.display.marioY += self.player.display.velocityY
        # Y軸方向の移動
        if self.player.display.marioY > 772:
            self.player.display.marioY = 772

        if self.player.display.marioY == 772:
            self.player.event.isJump["first"] = False
            self.player.event.isJump["jumping"] = False

        print(f"VelocityY: {self.player.display.velocityY}")

        # print(f"marioY: {self.player.display.marioY}")

    def getVelocity(self):
        # Y軸方向の速度を取得
        # a = self.event.isJump["first"]
        # i = self.event.isJump["jumping"]
        # print(f"state: {self.state} \n previousKeyEvent: {self.event.previousKeyEvent}")
        # print(f"first: {a} \n jumping: {i}")
        if self.player.event.state == 2 or self.player.event.state == 3:
            if self.player.event.isJump["jumping"] is True:
                if self.player.event.isJump["first"] is False:
                    self.player.event.isJump["first"] = True
                    self.player.display.velocityY = -12.5
                else:
                    if self.player.display.velocityY < 0:
                        self.player.display.velocityY += 0.3
                        if self.player.display.velocityY > -4:
                            self.player.display.velocityY += 0.5
                    else:
                        if self.player.display.velocityY < 12.5:
                            self.player.display.velocityY += 1.9
            return
        else:
            if self.player.display.velocityY < 12.5:
                self.player.display.velocityY += 1.9
