import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500))

def blit_list():
    for i in obstructions_list:
        sc.blit(i.image, i.rect)

def move_obstructions_in_list():
    for i in obstructions_list:
        i.rect.x -= MOVE_OBSTRUCTIONS

def generation_landscape_in_blocks(i):
    global point_blocks, r, stabilization
    if i.rect.right < 0:
        i.rect.x = 800
        r = random.randint(1, 3)
        if r > 2 and point_blocks < 1:
            i.rect.y -= 100
            point_blocks += 1
            print(r)
        elif r < 2 and point_blocks > 0:
            i.rect.y += 100
            point_blocks -= 1
            print(r)
        elif 1 < r < 3:
            # тут ничего не делается, просто для понятия создал это условие
            print(r)
        if point_blocks == 0:
            i.rect.bottom = 650
        elif point_blocks == 1:
            i.rect.bottom = 550
        elif point_blocks == 2:
            i.rect.bottom = 450
        elif point_blocks == 3:
            i.rect.bottom = 350
        elif point_blocks == 4:
            i.rect.bottom = 250



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
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

class ObstrucTion(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))

airship = AirShip(50, 100, 'airship_texture.png')
airship_mask = pygame.mask.from_surface(airship.image)
airship_y = 0
direction = 0
gravitation = 0
number_gravitation = 1
rotate = 1
point_blocks = 0
MOVE_OBSTRUCTIONS = 30

obstructions_list = []
obstructions_list_masks = []
obstructions_list.append(ObstrucTion(900, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[0].image))
obstructions_list.append(ObstrucTion(830, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[1].image))
obstructions_list.append(ObstrucTion(760, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[2].image))
obstructions_list.append(ObstrucTion(690, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[3].image))
obstructions_list.append(ObstrucTion(620, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[4].image))
obstructions_list.append(ObstrucTion(550, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[5].image))
obstructions_list.append(ObstrucTion(480, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[6].image))
obstructions_list.append(ObstrucTion(410, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[7].image))
obstructions_list.append(ObstrucTion(340, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[8].image))
obstructions_list.append(ObstrucTion(270, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[9].image))
obstructions_list.append(ObstrucTion(100, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[10].image))
obstructions_list.append(ObstrucTion(30, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[11].image))
obstructions_list.append(ObstrucTion(-40, 400, 'obstruction_texture.png'))
obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[12].image))


clock = pygame.time.Clock()
FPS = 30

r = random.randint(1, 3)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    speed_fall()
    touch()

    smoothness_rotate()


    sc.fill((99, 24, 16))

    sc.blit(airship.image, airship.rect)
    pygame.draw.rect(sc, (255, 255, 255), pygame.Rect(airship), 1)
    clock.tick(FPS)
    move_obstructions_in_list()
    blit_list()
    for i in obstructions_list:
        generation_landscape_in_blocks(i)

    # offset = (obstruction.rect.x - airship.rect.x, obstruction.rect.y - airship.rect.y)
    # if airship_mask.overlap_area(obstruction_mask, offset) > 0:
    #     print('пересечение')
    pygame.display.update()
    print(obstructions_list[0].rect.y)