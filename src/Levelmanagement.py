class LevelManagement:
    level = 0
    creatureAmount = 0
    creatureSpeed = 0
    creatureFireRate = 0
    shipSpeed = 0
    maxShipSpeed = 0
    maxCreatureSpeed = 0
    backgroundSpeed = 0
    maxBackgroundSpeed = 0

    def nextLevel(self):
        self.level += 1

    def getLevel(self):
        return self.level