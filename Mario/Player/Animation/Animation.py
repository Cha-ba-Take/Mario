from Player.Animation import AnimationData


class animation:
    def __init__(self, player):
        self.player = player

    def animation(self):
        # プレイヤーのアニメーション
        data = AnimationData.data(self.player)
        self.player.image = self.player.animator.getImage(self.player.display.frame, data.getAnimationData())
