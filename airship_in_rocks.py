import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500))

class AirShip(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))

airship = AirShip(50, 250, 'airship_texture.png')
gravitation = 0
number_gravitation = 0

clock = pygame.time.Clock()
FPS = 60

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    gravitation -= 1

    sc.fill((0, 0, 0))
    if number_gravitation % 2 == 0:
        number_gravitation += 0.2
        airship.rect.y -= gravitation
    else:
        number_gravitation += 0.2
    pygame.display.update()
    sc.blit(airship.image, airship.rect)
    clock.tick(FPS)
    pygame.display.update()