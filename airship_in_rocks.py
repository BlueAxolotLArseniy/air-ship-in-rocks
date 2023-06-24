import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500))

def speed_fall():
    global gravitation, number_gravitation
    gravitation -= 1

    if pygame.mouse.get_pressed()[0]:
        gravitation += 3
    if number_gravitation % 1 == 0:
        number_gravitation += 1
        airship.rect.y -= gravitation
    else:
        number_gravitation += 1

def smoothness_rotate():
    global airship, direction
    airship_y = airship.rect.y
    airship.image = pygame.transform.rotate(airship.original_image, gravitation)  # Поворот в обратном направлении на 5 градусов
    airship.rect = airship.image.get_rect(center=airship.rect.center)  # Обновление rect с новым положением
    if gravitation < 0:
        direction -= gravitation
    if gravitation > 0:
        direction += gravitation


def touch():
    global gravitation
    if airship.rect.bottom >= 501:
        airship.rect.bottom = 500
        gravitation = 0
    if airship.rect.top <= -1:
        airship.rect.top = 1
        gravitation = 0

class AirShip(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

airship = AirShip(50, 250, 'airship_texture.png')
airship_y = 0
direction = 0
gravitation = 0
number_gravitation = 1
rotate = 1

clock = pygame.time.Clock()
FPS = 30

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    speed_fall()
    touch()

    # if gravitation < 6 and direction >= 10:
    #     airship_y = airship.rect.y
    #     airship.image = pygame.transform.rotate(airship.original_image, -5)  # Поворот в обратном направлении на 5 градусов
    #     airship.rect = airship.image.get_rect(center=airship.rect.center)  # Обновление rect с новым положением
    #     direction -= 5
    # if gravitation > 3 and direction <= 10:
    #     airship_y = airship.rect.y
    #     airship.image = pygame.transform.rotate(airship.original_image, 5)  # Поворот на 5 градусов
    #     airship.rect = airship.image.get_rect(center=airship.rect.center)  # Обновление rect с новым положением
    #     direction += 5
    smoothness_rotate()


    sc.fill((0, 0, 0))


    sc.blit(airship.image, airship.rect)
    clock.tick(FPS)
    pygame.display.update()