import random
from Window import WIDTH, HEIGHT
from Graphics import Graphics
from Movement import Movement
from Route import Route


class Creature(Graphics, Movement):
    hp = None
    route = None

    def __init__(self, hp):
        self.hp = hp
        Graphics.__init__(self, f'../graphics/creature-{random.randint(10, 39)}.png')
        Movement.__init__(self, random.randint(1, 5))
        self.scaleUp(random.uniform(0.5, 1.5))
        self.xPos = random.randint(self.getWidth(), WIDTH - self.getWidth())
        self.yPos = random.randint(-200, -self.getHeight())
        self.route = Route(self.getWidth(), self.getHeight(), self.speed)

    def move(self):
        if self.route.isFinished():
            self.route.newRoute(self.xPos, self.yPos)
        self.setXPos(self.route.getNextPoint(self.xPos, self.yPos).x)
        self.setYPos(self.route.getNextPoint(self.xPos, self.yPos).y)

    def isOutOfBounds(self):
        return self.yPos > HEIGHT