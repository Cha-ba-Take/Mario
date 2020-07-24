# -*- coding: UTF-8-*-

from Player.Animation import AnimationDataList


class AnimationData:
    def __init__(self, player):
        self.player = player
        self.state = self.player.event.state
        self.isJump = self.player.event.isJump
        self.animationData = None

    def getAnimationData(self):
        # プレイヤーのアニメーションデータを取得
        if self.state == 0:
            if self.player.direction:
                self.animationData = AnimationDataList.RIGHT_IDLE
            else:
                self.animationData = AnimationDataList.LEFT_IDLE
        elif self.state == 1:
            if self.player.direction:
                self.animationData = AnimationDataList.RIGHT_WALK
            else:
                self.animationData = AnimationDataList.LEFT_WALK

        if self.isJump["jumping"]:
            if self.player.direction:
                self.animationData = AnimationDataList.RIGHT_JUMP
            else:
                self.animationData = AnimationDataList.LEFT_JUMP
        else:
            if self.state == 2:
                if self.player.direction:
                    self.animationData = AnimationDataList.RIGHT_IDLE
                else:
                    self.animationData = AnimationDataList.LEFT_IDLE
            if self.state == 3:
                if self.player.direction:
                    self.animationData = AnimationDataList.RIGHT_WALK
                else:
                    self.animationData = AnimationDataList.LEFT_WALK
        return self.animationData
