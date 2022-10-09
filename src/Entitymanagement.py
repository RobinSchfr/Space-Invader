from Creature import Creature
from Game import Game


class EntityManagement:
    creatureCount = None
    game = None
    creatures = []
    playerBullets = []
    hostileBullets = []

    def __init__(self, gameInstance):
        self.creatureCount = 1
        self.game = gameInstance

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

    def getCreatures(self):
        return self.creatures

    def getPlayerBullets(self):
        return self.playerBullets

    def getHostileBullets(self):
        return self.hostileBullets

    def getEntities(self):
        return self.creatures + self.playerBullets + self.hostileBullets