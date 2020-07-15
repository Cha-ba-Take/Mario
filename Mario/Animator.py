# -*- coding: UTF-8 -*-


class Animator:
    def __init__(self, images):
        self.images = images

    def getImage(self, frame, animationData):
        # アニメーションデータからアニメーション画像を取得
        times = animationData[0]
        locate = animationData[1]
        animationCycle = animationData[2]
        index = locate if animationCycle is None else int(frame / animationCycle % times) + locate
        return self.images[index]
