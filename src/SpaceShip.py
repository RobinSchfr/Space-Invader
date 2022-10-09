from Game import Game
from Graphics import Graphics
from Laserbullet import Laserbullet


class SpaceShip(Graphics):
    entityManagement = None
    hp = 0
    
    def __init__(self, path, speed, entityManagement, hp):
        super().__init__(path, speed)
        self.scaleUp()
        self.entityManagement = entityManagement
        self.hp = hp
        self.xPos = Game.WIDTH / 2 - self.getWidth() / 2
        self.yPos = Game.HEIGHT - 150

    def fire(self):
        bullet = Laserbullet(self.xPos, self.yPos, True)
        self.entityManagement.getPlayerBullets().append(bullet)