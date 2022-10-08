from Creature import Creature


class CreaturesManagment:
    creatures = []
    creatureCount = None

    def __init__(self):
        self.creatureCount = 1
        self.spawnCreature()
        self.spawnCreature()
        self.spawnCreature()
        self.spawnCreature()
        self.spawnCreature()

    def spawnCreature(self):
        c = Creature(1)
        self.creatures.append(c)

    def update(self):
        for creature in self.creatures:
            if creature.isOutOfBounds():
                self.creatures.remove(creature)