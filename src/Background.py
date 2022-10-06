class Background:
    y = 0
    background = None
    height = None
    movingSpeed = None

    def __init__(self, bg, movingSpeed):
        self.background = bg
        self.height = bg
        self.movingSpeed = movingSpeed

    def shiftDown(self):
        self.y += self.movingSpeed
        if self.y > self.background.get_size()[1]:
            self.y = 0

    def getY(self):
        return self.y

    def getBg(self):
        return self.background