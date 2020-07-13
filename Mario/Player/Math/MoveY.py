from abc import ABC

from Player.Math import Move


class MoveY(Move.Move, ABC):
    def __init__(self, player):
        self.player = player
        self.state = self.player.state

    def move(self):
        # Y軸方向の移動
        self.getVelocity()

    def getVelocity(self):
        # Y軸方向の速度を取得
        if self.state == 0:
            self.player.velocityY = 0
