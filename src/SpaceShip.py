from Window import WIDTH, HEIGHT
from Graphics import Graphics
from Movement import Movement


class SpaceShip(Graphics, Movement):
    hp = 0
    
    def __init__(self, path, speed, hp):
        Graphics.__init__(self, path)
        Movement.__init__(self, speed)
        self.scaleUp()
        self.hp = hp
        self.xPos = WIDTH / 2 - self.getWidth() / 2
        self.yPos = HEIGHT - 150