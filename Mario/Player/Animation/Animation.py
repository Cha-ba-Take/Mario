# -*- coding: UTF-8 -*-

from Player.Animation import AnimationData


class Animation:
    def __init__(self, player):
        self.player = player

    def playerAnimation(self):
        # プレイヤーのアニメーション
        data = AnimationData.AnimationData(self.player)
        self.player.image = self.player.animator.getImage(self.player.display.frame, data.getAnimationData())
