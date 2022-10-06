import pygame
import sys
import Background as Bg
import SpaceShip as Ship

WIDTH = 800
HEIGHT = 950


class Game:
    FPS = 75
    screen = None
    clock = None
    bg = None
    bgStars = None
    ship = None
    creatures = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Invader')
        self.clock = pygame.time.Clock()
        self.bg = Bg.Background('../graphics/Background.png', 3)
        self.bgStars = Bg.Background('../graphics/Background_stars.png', 1)
        self.ship = Ship.SpaceShip('../graphics/spaceship-1.png', 2)

    def draw(self):
        self.drawBG()
        self.drawShip()
        pygame.display.flip()

    def drawBG(self):
        self.screen.blit(self.bg.getImage(), (0, self.bg.getY()-self.bg.getHeight()))
        self.screen.blit(self.bg.getImage(), (0, self.bg.getY()))
        self.screen.blit(self.bgStars.getImage(), (0, self.bgStars.getY() - self.bgStars.getHeight()))
        self.screen.blit(self.bgStars.getImage(), (0, self.bgStars.getY()))

    def drawShip(self):
        self.screen.blit(self.ship.getImage(), (self.ship.getXPos(), self.ship.getYPos()))
        print(self.ship.getXPos(), self.ship.getYPos())

    def shiftBG(self):
        self.bg.shiftDown()
        self.bgStars.shiftDown()

    def main(self):
        while True:
            self.handleEvents()
            self.shiftBG()
            self.draw()
            self.clock.tick(self.FPS)

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