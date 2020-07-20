from abc import ABC

from Player.Move import Move


class MoveY(Move.Move, ABC):
    def __init__(self, player):
        self.player = player
        self.state = self.player.state

    def move(self):
        # Y軸方向の移動
        self.getVelocity()
        self.player.display.marioY -= self.player.display.velocityY

    def getVelocity(self):
        # Y軸方向の速度を取得
        if self.state == 0:
            self.player.display.velocityY = 0
        elif self.state == 4:
            self.player.display.velocityY = 3
