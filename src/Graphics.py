from Game import Game
import pygame


class Graphics:
    image = None
    movingSpeed = None
    hitbox = None
    xPos = None
    yPos = None

    def __init__(self, path, movingSpeed):
        self.image = pygame.image.load(path)
        self.movingSpeed = movingSpeed
        self.hitbox = self.image.get_rect()

    def getImage(self):
        return self.image

    def getWidth(self):
        return self.image.get_width()

    def getHeight(self):
        return self.image.get_height()

    def setMovingSpeed(self, val):
        self.movingSpeed = val

    def moveUp(self, openBounds=False):
        if self.yPos > 0 or openBounds:
            self.yPos -= 1 * self.movingSpeed
            self.hitbox.y = self.yPos

    def moveDown(self, openBounds=False):
        if self.yPos < Game.HEIGHT - self.getHeight() or openBounds:
            self.yPos += 1 * self.movingSpeed / 2
            self.hitbox.y = self.yPos

    def moveLeft(self):
        if self.xPos > 0:
            self.xPos -= 1 * self.movingSpeed
            self.hitbox.x = self.xPos

    def moveRight(self):
        if self.xPos < Game.WIDTH - self.getWidth():
            self.xPos += 1 * self.movingSpeed
            self.hitbox.x = self.xPos

    def setXPos(self, val):
        self.xPos = self.hitbox.x = val

    def setYPos(self, val):
        self.yPos = self.hitbox.y = val

    def scaleUp(self, k=1):
        self.image = pygame.transform.scale(self.image, (100 * k, 100 * k))
        self.hitbox = self.image.get_rect()

    def getMovingSpeed(self):
        return self.movingSpeed

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def getHitbox(self):
        return self.hitbox

    def isOutOfBounds(self):
        pass