import pygame


class Graphics:
    image = None

    def __init__(self, path):
        self.image = pygame.image.load(path)

    def getImage(self):
        return self.image

    def getWidth(self):
        return self.image.get_width()

    def getHeight(self):
        return self.image.get_height()

    def scaleUp(self):
        self.image = pygame.transform.scale(self.image, (100, 100))