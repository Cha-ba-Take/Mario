from abc import ABC

from Player.Move import Move


class MoveY(Move.Move, ABC):
    def __init__(self, player):
        self.player = player
        self.state = self.player.state

    def move(self):
        self.getVelocity()
        self.player.display.marioY += self.player.display.velocityY
        # Y軸方向の移動
        if self.player.display.marioY > 772:
            self.player.display.marioY -= self.player.display.velocityY

    def getVelocity(self):
        # Y軸方向の速度を取得
        if self.state == 0:
            self.player.display.velocityY = 5

        if self.player.is_jump is True:
            if self.player.display.velocityY < 0:
                self.player.display.velocityY += 0.125

            elif self.player.display.velocityY == 0:
                self.player.display.velocityY = -4
