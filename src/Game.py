import pygame
import sys
from Window import WIDTH, HEIGHT
from Background import Background
from SpaceShip import SpaceShip
from Creaturesmanagement import CreaturesManagement
from Levelmanagement import LevelManagement


class Game:
    FPS = 75
    screen = None
    clock = None
    bg = None
    bgStars = None
    ship = None
    creaturesManagement = None
    levelManagement = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Invader')
        self.clock = pygame.time.Clock()
        self.bg = Background('../graphics/Background.png', 2)
        self.bgStars = Background('../graphics/Background_stars.png', 1)
        self.ship = SpaceShip('../graphics/spaceship-1.png', 2, 5)
        self.creaturesManagement = CreaturesManagement()
        self.levelManagement = LevelManagement()

    def draw(self):
        self.drawBG()
        self.drawCreatures()
        self.drawShip()
        self.drawLevel()
        pygame.display.flip()

    def drawBG(self):
        self.screen.blit(self.bg.getImage(), (0, self.bg.getY() - self.bg.getHeight()))
        self.screen.blit(self.bg.getImage(), (0, self.bg.getY()))
        self.screen.blit(self.bgStars.getImage(), (0, self.bgStars.getY() - self.bgStars.getHeight()))
        self.screen.blit(self.bgStars.getImage(), (0, self.bgStars.getY()))

    def drawLevel(self):
        font = pygame.font.SysFont('Consolas', 30)
        scoreLabel = font.render(str(self.levelManagement.getLevel()).zfill(3), True, pygame.Color('#00ffff'))
        self.screen.blit(scoreLabel, (5, 5))

    def drawCreatures(self):
        self.creaturesManagement.update()
        for creature in self.creaturesManagement.creatures:
            creature.move()
            self.screen.blit(creature.getImage(), (creature.getXPos(), creature.getYPos()))

    def drawShip(self):
        self.screen.blit(self.ship.getImage(), (self.ship.getXPos(), self.ship.getYPos()))

    def shiftBG(self):
        self.bg.shiftDown()
        self.bgStars.shiftDown()

    def main(self):
        while True:
            self.handleEvents()
            self.shiftBG()
            self.draw()
            self.checkForCollision()
            self.clock.tick(self.FPS)

    def checkForCollision(self):
        for creature in self.creaturesManagement.getCreatures():
            if self.ship.getHitbox().colliderect(creature.getHitbox()):
                print('Hit')

    def handleEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.ship.moveUp()
        if keys[pygame.K_s]:
            self.ship.moveDown()
        if keys[pygame.K_a]:
            self.ship.moveLeft()
        if keys[pygame.K_d]:
            self.ship.moveRight()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def quit(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    g = Game()
    g.main()