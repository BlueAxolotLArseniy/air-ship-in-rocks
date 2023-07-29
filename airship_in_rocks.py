import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

def offest_list():
    for i in range(len(obstructions_list)):
        if airship_mask.overlap_area(obstructions_list_masks[i], (obstructions_list[i].rect.x - airship.rect.x, obstructions_list[i].rect.y - airship.rect.y)) > 0:
            print('пересечение')

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
        elif r < 2 and point_blocks > 0:
            i.rect.y += 100
            point_blocks -= 1
        elif 1 < r < 3:
            pass
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
    airship.image = pygame.transform.rotate(airship.original_image, gravitation*1.5)  # Поворот в обратном направлении на 5 градусов
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
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

class ObstrucTion(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
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

obstruction = ObstrucTion(800*3/2, 250, 'obstruction_texture56.png')
obstruction_mask = pygame.mask.from_surface(obstruction.image)
obstruction2 = ObstrucTion(800*3/2+2400, 250, 'obstruction_texture56.png')
obstruction_mask2 = pygame.mask.from_surface(obstruction2.image)

# obstructions_list = []
# obstructions_list_masks = []
# obstructions_list.append(ObstrucTion(900, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[0].image))
# obstructions_list.append(ObstrucTion(830, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[1].image))
# obstructions_list.append(ObstrucTion(760, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[2].image))
# obstructions_list.append(ObstrucTion(690, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[3].image))
# obstructions_list.append(ObstrucTion(620, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[4].image))
# obstructions_list.append(ObstrucTion(550, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[5].image))
# obstructions_list.append(ObstrucTion(480, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[6].image))
# obstructions_list.append(ObstrucTion(410, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[7].image))
# obstructions_list.append(ObstrucTion(340, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[8].image))
# obstructions_list.append(ObstrucTion(270, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[9].image))
# obstructions_list.append(ObstrucTion(100, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[10].image))
# obstructions_list.append(ObstrucTion(30, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[11].image))
# obstructions_list.append(ObstrucTion(-40, 400, 'obstruction_texture.png'))
# obstructions_list_masks.append(pygame.mask.from_surface(obstructions_list[12].image))


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


    if obstruction.rect.right < 10:
        obstruction.rect.left = obstruction2.rect.right
        if random.randint(1, 2) == 2:
            obstruction.image = pygame.image.load("obstruction_texture57.png")
        else:
            obstruction.image = pygame.image.load("obstruction_texture56.png")
    if obstruction2.rect.right < 10:
        obstruction2.rect.left = obstruction.rect.right
        if random.randint(1, 2) == 2:
            obstruction2.image = pygame.image.load("obstruction_texture57.png")
        else:
            obstruction2.image = pygame.image.load("obstruction_texture56.png")


    sc.fill((30, 30, 30))
    sc.blit(obstruction.image, obstruction.rect)
    sc.blit(obstruction2.image, obstruction2.rect)
    obstruction.rect.x -= 20
    obstruction2.rect.x -= 20
    sc.blit(airship.image, airship.rect)
    # pygame.draw.rect(sc, (255, 255, 255), pygame.Rect(airship), 1)
    clock.tick(FPS)
    # move_obstructions_in_list()
    # blit_list()
    # for i in obstructions_list:
    #     generation_landscape_in_blocks(i)
    #
    # offest_list()
    pygame.display.update()
    # print(obstructions_list[0].rect.y)
    if airship_mask.overlap_area(obstruction_mask, (obstruction.rect.x - airship.rect.x, obstruction.rect.y - airship.rect.y)) > 0 or airship_mask.overlap_area(obstruction_mask2, (obstruction2.rect.x - airship.rect.x, obstruction2.rect.y - airship.rect.y)) > 0:
        print('пересечение')
