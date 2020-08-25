# -*- coding: UTF-8 -*-

class Move:
    def __init__(self, character):
        self.character = character

        self.horizontalVelocity = 0
        self.horizontalPhysicalData = self.character.constants["horizontalPhysicalData"]
        self.horizontalVelocityLimit = self.horizontalPhysicalData["velocityLimit"]
        self.horizontalStartingAcceleration = self.horizontalPhysicalData["startingAcceleration"]
        self.horizontalStoppingAcceleration = self.horizontalPhysicalData["stoppingAcceleration"]

        self.verticalVelocity = 0
        self.verticalPhysicalData = self.character.constants["verticalPhysicalData"]
        self.fallVelocityLimit = self.verticalPhysicalData["fallVelocityLimit"]
        self.fallAcceleration = self.verticalPhysicalData["fallAcceleration"]

        self.direction = 1

    def moveX(self):
        state = self.character.event.getState()

        if state == 0:
            self.stop()
        elif state == 1:
            if self.horizontalVelocity < 0:
                self.stop()
            else:
                self.direction = 1
                self.walk()
        elif state == 2:
            if self.horizontalVelocity > 0:
                self.stop()
            else:
                self.direction = -1
                self.walk()

        self.character.x += self.horizontalVelocity
        self.character.x = min(max(self.character.x, 0), 736)

    def stop(self):
        if self.horizontalVelocity > 0:
            self.horizontalVelocity += self.horizontalStoppingAcceleration
        elif self.horizontalVelocity < 0:
            self.horizontalVelocity += -self.horizontalStoppingAcceleration
        else:
            self.horizontalVelocity = 0

    def walk(self):
        if abs(self.horizontalVelocity) < self.horizontalVelocityLimit:
            self.horizontalVelocity += self.horizontalStartingAcceleration * self.direction
        else:
            self.horizontalVelocity = self.horizontalVelocityLimit * self.direction

    def moveY(self):
        self.fall()

        self.character.y += self.verticalVelocity
        self.character.y = min(self.character.y, 536)

    def fall(self):
        if self.verticalVelocity < self.fallVelocityLimit:
            self.verticalVelocity += self.fallAcceleration
        else:
            self.verticalVelocity = self.fallVelocityLimit

    def move(self):
        self.moveX()
        self.moveY()

    def getDirection(self):
        return self.direction
