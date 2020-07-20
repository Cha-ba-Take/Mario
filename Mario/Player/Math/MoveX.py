from abc import ABC

from Player.Math import Move


class MoveX(Move.Move, ABC):
    def __init__(self, player):
        self.player = player
        self.state = self.player.state

    def move(self):
        # X軸方向の移動
        self.getVelocity()
        self.player.display.marioX += self.player.display.velocityX
        self.player.display.marioX = min(max(self.player.display.marioX, 0), 512)

    def getVelocity(self):
        # X軸方向の速度を取得
        if self.state == 0:
            self.player.display.velocityX = 0
        elif self.state == 1:
            self.player.display.velocityX = 4
        elif self.state == 2:
            self.player.display.velocityX = -4
