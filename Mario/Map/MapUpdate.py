# -*- coding: UTF-8 -*-

from Map import Structure


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
            index = int(self.MapInstance.mapData[y][mapX])
            chip = self.MapInstance.chipList[index]
            position = (mapX * self.MapInstance.chipSize[0], y * self.MapInstance.chipSize[1])
            """if index in self.MapInstance.structureList:
                structure = Structure.Structure(self, chip, position)
                self.MapInstance.display.collide.blocks.add(structure)
                self.MapInstance.display.collide.blocks.draw(self.MapInstance.map)
            else:"""
            self.MapInstance.map.blit(chip, position)
