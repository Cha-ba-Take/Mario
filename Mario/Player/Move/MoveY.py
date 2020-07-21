from abc import ABC

from Player.Move import Move


class MoveY(Move.Move, ABC):
    def __init__(self, player, event):
        self.player = player
        self.event = event
        self.state = self.player.state

    def move(self):
        self.getVelocity()
        self.player.display.marioY += self.player.display.velocityY
        # Y軸方向の移動
        if self.player.display.marioY > 772:
            self.player.display.marioY = 772

        if self.player.display.marioY == 772:
            self.event.is_jump["first"] = False
            self.event.is_jump["jumping"] = False

        # print(f"marioY: {self.player.display.marioY}")

    def getVelocity(self):
        # Y軸方向の速度を取得
        # a = self.event.is_jump["first"]
        # i = self.event.is_jump["jumping"]
        # print(f"state: {self.state} \n previousKeyEvent: {self.event.previousKeyEvent}")
        # print(f"first: {a} \n jumping: {i}")
        if self.state == 4:
            if self.event.previousKeyEvent == 0 and self.event.is_jump["jumping"] is True:
                if self.event.is_jump["first"] is False:
                    self.event.is_jump["first"] = True
                    self.player.display.velocityY = -7
                else:
                    self.player.display.velocityY += 0.125
            else:
                self.player.display.velocityY += 0.125
        else:
            self.player.display.velocityY = 5
