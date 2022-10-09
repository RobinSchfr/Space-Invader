from Game import Game
from Graphics import Graphics
from Route import Route
import random


class Creature(Graphics):
    hp = None
    route = None

    def __init__(self, hp):
        self.hp = hp
        super().__init__(f'../graphics/creature-{random.randint(10, 39)}.png', random.randint(1, 5))
        self.scaleUp(random.uniform(0.5, 1.5))
        self.xPos = random.randint(self.getWidth(), Game.WIDTH - self.getWidth())
        self.yPos = random.randint(-200, -self.getHeight())
        self.route = Route(self.getWidth(), self.getHeight(), self.movingSpeed)

    def move(self):
        if self.route.isFinished():
            self.route.newRoute(self.xPos, self.yPos)
        self.setXPos(self.route.getNextPoint(self.xPos, self.yPos).x)
        self.setYPos(self.route.getNextPoint(self.xPos, self.yPos).y)

    def isOutOfBounds(self):
        return self.yPos > Game.HEIGHT