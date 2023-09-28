import pygame

pygame.init()

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect(center=(x, y))

screen = pygame.display.set_mode((720,480))
screen.fill((0, 230, 30))

clock = pygame.time.Clock()
FPS = 30

while True:
    screen.fill((0, 230, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit()

    pygame.display.update()