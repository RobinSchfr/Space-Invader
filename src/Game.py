import pygame
import sys
import ImageLoader as Il
import Background as Bg


class Game:
    WIDTH = 800
    HEIGHT = 900
    FPS = 75
    screen = None
    clock = None
    bg = None
    bgStars = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Invader")
        self.clock = pygame.time.Clock()
        self.bg = Bg.Background(Il.bg, 3)
        self.bgStars = Bg.Background(Il.bgStars, 1)

    def draw(self):
        self.drawBG()
        x = pygame.transform.scale(Il.monster, (100, 100))
        self.screen.blit(x, (400-x.get_size()[0]/2, 20))
        pygame.display.flip()

    def drawBG(self):
        self.screen.blit(self.bg.getBg(), (0, self.bg.getY()-self.bg.getBg().get_size()[1]))
        self.screen.blit(self.bg.getBg(), (0, self.bg.getY()))
        # pygame.draw.line(self.screen, (200, 0, 0), (0, self.bg.getY()), (800, self.bg.getY()))
        self.screen.blit(self.bgStars.getBg(), (0, self.bgStars.getY() - self.bgStars.getBg().get_size()[1]))
        self.screen.blit(self.bgStars.getBg(), (0, self.bgStars.getY()))

    def shiftBG(self):
        self.bg.shiftDown()
        self.bgStars.shiftDown()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.shiftBG()
            self.draw()
            self.clock.tick(self.FPS)


g = Game()
g.main()