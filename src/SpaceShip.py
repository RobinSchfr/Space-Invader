from Game import Game
from Graphics import Graphics


class SpaceShip(Graphics):
    hp = 0
    
    def __init__(self, path, speed, hp):
        super().__init__(path, speed)
        self.scaleUp()
        self.hp = hp
        self.xPos = Game.WIDTH / 2 - self.getWidth() / 2
        self.yPos = Game.HEIGHT - 150

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos