import pygame.transform

from Game import Game
from Graphics import Graphics


class Laserbullet(Graphics):
    isPlayerBullet = None

    def __init__(self, xPos, yPos, isPlayerBullet):
        if isPlayerBullet:
            super().__init__('../graphics/laserBlue01.png', 5)
            self.xPos = xPos + 46
            self.yPos = yPos
        else:
            super().__init__('../graphics/laserRed01.png', 5)
            self.image = pygame.transform.rotate(self.image, 180)
            self.xPos = xPos + 46
            self.yPos = yPos + 0
        self.isPlayerBullet = isPlayerBullet

    def move(self):
        if self.isPlayerBullet:
            self.moveUp(True)
        else:
            self.moveDown(True)

    def isOutOfBounds(self):
        if self.isPlayerBullet:
            return self.yPos + self.getHeight() < 0
        return self.yPos > Game.HEIGHT