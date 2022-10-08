from Creature import Creature


class CreaturesManagment:
    creatures = []
    creatureCount = None

    def __init__(self):
        self.creatureCount = 5

    def spawnCreature(self):
        currentCreatures = len(self.creatures)
        for i in range(self.creatureCount - currentCreatures):
            c = Creature(1)
            self.creatures.append(c)

    def update(self):
        self.spawnCreature()
        for creature in self.creatures:
            if creature.isOutOfBounds():
                self.creatures.remove(creature)