import Game
import Graphics


class SpaceShip(Graphics.Graphics):
    xPos = 0
    yPos = 0
    speed = 0

    def __init__(self, path, speed):
        super().__init__(path)
        self.scaleUp()
        self.speed = speed
        self.xPos = Game.WIDTH / 2 - self.getWidth() / 2
        self.yPos = Game.HEIGHT - 150

    def moveUp(self):
        if self.yPos > 0:
            self.yPos -= 1 * self.speed

    def moveDown(self):
        if self.yPos < Game.HEIGHT - self.getHeight():
            self.yPos += 1 * self.speed

    def moveLeft(self):
        if self.xPos > 0:
            self.xPos -= 1 * self.speed

    def moveRight(self):
        if self.xPos < Game.WIDTH - self.getWidth():
            self.xPos += 1 * self.speed

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos