from Player.Move import MoveX
from Player.Move import MoveY

from Player.Animation import Animation


class update:
    def __init__(self, player):
        self.player = player

    def update(self, event):
        # プレイヤーの更新
        event.stateMachine()
        self.player.state = event.state
        self.player.previousState = event.previousState
        self.player.previousKeyEvent = event.previousKeyEvent
        self.player.is_jump = event.is_jump

        self.move(event)
        Animation.animation(self.player).animation()

    def move(self, event):
        # プレイヤーの移動
        MoveX.MoveX(self.player, event).move()
        MoveY.MoveY(self.player, event).move()
        self.player.rect = self.player.image.get_rect(topleft=(self.player.display.marioX, self.player.display.marioY))
