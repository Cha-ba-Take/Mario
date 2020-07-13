class update:
    def __init__(self, Map):
        self.MapInstance = Map
        self.MapInstance.previousWorldX = self.MapInstance.worldX
        self.scroll()
        self.blit()

    def scroll(self):
        if self.checkScroll() is False:
            return

        self.MapInstance.map.scroll(-64, 0)

    def checkScroll(self):
        if self.MapInstance.display.marioX == 512:
            self.MapInstance.worldX += self.MapInstance.display.velocityX

        if self.MapInstance.previousWorldX % 64 <= self.MapInstance.worldX % 64: return False
        return True

    def blit(self):
        mapX = int(self.MapInstance.worldX // 64) + 17
        for y in range(15):
            chip = self.MapInstance.chipList[int(self.MapInstance.mapData[y][mapX])]
            position = (mapX * self.MapInstance.chipSize[0], y * self.MapInstance.chipSize[1])
            self.MapInstance.map.blit(chip, position)