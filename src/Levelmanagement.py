class LevelManagement:
    level = 0
    game = None
    creatureAmount = 0
    creatureSpeed = 0
    creatureFireRate = 0
    shipSpeed = 0
    shipFireRate = 0
    maxShipSpeed = 0
    maxCreatureSpeed = 0
    backgroundSpeed = 0
    maxBackgroundSpeed = 0

    def __init__(self, gameInstance):
        self.game = gameInstance

    def nextLevel(self):
        self.level += 1

    def getLevel(self):
        return self.level