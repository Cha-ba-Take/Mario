from Player.Animation import AnimationDataList


class data:
    def __init__(self, player):
        self.player = player
        self.state = self.player.state
        self.animationData = None

    def getAnimationData(self):
        # プレイヤーのアニメーションデータを取得
        if self.state == 0:
            self.animationData = AnimationDataList.IDLE
        elif self.state == 1:
            self.animationData = AnimationDataList.LEFT
        elif self.state == 2:
            self.animationData = AnimationDataList.RIGHT
        elif self.state == 4 or self.state == 5:
            self.animationData = AnimationDataList.JUMP
        return self.animationData
