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

class ObstrucTion(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))

airship = AirShip(50, 250, 'airship_texture.png')
airship_mask = pygame.mask.from_surface(airship.image)
lina = pygame.draw.line(sc, (255, 255, 255), (50, 300), (100, 400))
airship_y = 0
direction = 0
gravitation = 0
number_gravitation = 1
rotate = 1

obstruction = ObstrucTion(800, 450, 'obstruction_texture.png')
obstruction_mask = pygame.mask.from_surface(obstruction.image)

clock = pygame.time.Clock()
FPS = 30

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    speed_fall()
    touch()

    smoothness_rotate()


    sc.fill((0, 0, 0))

    sc.blit(airship.image, airship.rect)
    sc.blit(obstruction.image, obstruction.rect)
    pygame.draw.rect(sc, (255, 255, 255), pygame.Rect(airship), 1)
    clock.tick(FPS)
    sc.blit(lina.)
    pygame.display.update()
    obstruction.rect.x -= 13
    if obstruction.rect.right < 0:
        obstruction.rect.x = 800
        obstruction.rect.bottom = 500
    offset = (obstruction.rect.x - airship.rect.x, obstruction.rect.y - airship.rect.y)
    if airship_mask.overlap_area(obstruction_mask, offset) > 0:
        print('пересечение')