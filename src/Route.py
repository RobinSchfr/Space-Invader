import random
import pygame
from Window import WIDTH, HEIGHT


class Route:
    width = None
    height = None
    speed = None
    dest = None
    directionVector = None
    newPoint = None

    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed

    def newRoute(self, xPos, yPos):
        origin = pygame.Vector2(xPos, yPos)
        self.dest = pygame.Vector2(random.randint(self.width, WIDTH - self.width), random.randint(int(yPos) + 5, int(yPos) + random.randint(20, 120)))
        self.directionVector = self.dest - origin
        self.directionVector = self.directionVector.normalize() * self.speed

    def getNextPoint(self, xPos, yPos):
        oldPoint = pygame.Vector2(xPos, yPos)
        self.newPoint = oldPoint + self.directionVector
        return self.newPoint

    def isFinished(self):
        if self.newPoint is None or self.newPoint.distance_to(self.dest) <= self.speed:
            return True
        return False