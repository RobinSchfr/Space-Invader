from Creature import Creature
from Laserbullet import Laserbullet
from SpaceShip import SpaceShip


class EntityManagement:
    creatureCount = None
    game = None
    ship = None
    creatures = []
    playerBullets = []
    hostileBullets = []

    def __init__(self, gameInstance):
        self.creatureCount = 2
        self.game = gameInstance
        self.ship = SpaceShip('../graphics/spaceship-1.png', 2, 5)

    def spawnCreature(self):
        currentCreatures = len(self.creatures)
        for i in range(self.creatureCount - currentCreatures):
            c = Creature(1)
            self.creatures.append(c)

    def update(self):
        self.spawnCreature()
        for entity in self.getEntities():
            if entity.isOutOfBounds():
                if entity in self.creatures:
                    collection = self.creatures
                elif entity in self.playerBullets:
                    collection = self.playerBullets
                else:
                    collection = self.hostileBullets
                collection.remove(entity)

    def checkForCollision(self):
        for creature in self.creatures:
            if self.ship.getHitbox().colliderect(creature.getHitbox()):
                print('Hit')
            for bullet in self.playerBullets:
                if creature.getHitbox().collidepoint(bullet.xPos + bullet.getWidth() / 2, bullet.yPos):
                    print('Bullet hit')
                    self.creatures.remove(creature)

    def fire(self):
        bullet = Laserbullet(self.ship.getXPos(), self.ship.getYPos(), True)
        self.playerBullets.append(bullet)

    def getShip(self):
        return self.ship

    def getCreatures(self):
        return self.creatures

    def getPlayerBullets(self):
        return self.playerBullets

    def getHostileBullets(self):
        return self.hostileBullets

    def getEntities(self):
        return self.creatures + self.playerBullets + self.hostileBullets