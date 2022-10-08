from Window import WIDTH, HEIGHT


class Movement:
    speed = None
    xPos = None
    yPos = None

    def __init__(self, speed):
        self.speed = speed

    def moveUp(self):
        if self.yPos > 0:
            self.yPos -= 1 * self.speed

    def moveDown(self):
        if self.yPos < HEIGHT - self.getHeight():
            self.yPos += 1 * self.speed / 2

    def moveLeft(self):
        if self.xPos > 0:
            self.xPos -= 1 * self.speed

    def moveRight(self):
        if self.xPos < WIDTH - self.getWidth():
            self.xPos += 1 * self.speed

    def setXPos(self, val):
        self.xPos = val

    def setYPos(self, val):
        self.yPos = val

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def getSpeed(self):
        return self.speed