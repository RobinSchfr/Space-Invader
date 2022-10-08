import Graphics


class Background(Graphics.Graphics):
    yPos = 0

    def __init__(self, path, movingSpeed):
        super().__init__(path, movingSpeed)

    def shiftDown(self):
        self.yPos += self.movingSpeed
        if self.yPos > self.getHeight():
            self.yPos = 0

    def getY(self):
        return self.yPos