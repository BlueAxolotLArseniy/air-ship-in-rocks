import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

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
    def cheange_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))

class Buttons_in_menu(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

airship = AirShip(50, 100, 'airship_texture.png')
airship_mask = pygame.mask.from_surface(airship.image)
airship_y = 0
direction = 0
gravitation = 0
number_gravitation = 1
rotate = 1
MOVE_OBSTRUCTIONS = 30

button_play = Buttons_in_menu(400, 150, 'Button.png')
obstruction = ObstrucTion(800*3/2, 250, 'obstruction_texture56.png')
obstruction_mask = pygame.mask.from_surface(obstruction.image)
obstruction2 = ObstrucTion(800*3/2+2400, 250, 'obstruction_texture56.png')
obstruction_mask2 = pygame.mask.from_surface(obstruction2.image)

clock = pygame.time.Clock()
FPS = 30

r = random.randint(1, 3)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        sc.fill((30, 30, 30))

    # if menu == False:
        speed_fall()
        touch()

        smoothness_rotate()


        if obstruction.rect.right < 10:
            obstruction.rect.left = obstruction2.rect.right
            if random.randint(1, 2) == 2:
                obstruction.cheange_image("obstruction_texture57.png")
            else:
                obstruction.cheange_image("obstruction_texture56.png")
        if obstruction2.rect.right < 10:
            obstruction2.rect.left = obstruction.rect.right
            if random.randint(1, 2) == 2:
                obstruction2.cheange_image("obstruction_texture57.png")
            else:
                obstruction2.cheange_image("obstruction_texture56.png")



        sc.blit(obstruction.image, obstruction.rect)
        sc.blit(obstruction2.image, obstruction2.rect)
        obstruction.rect.x -= 20
        obstruction2.rect.x -= 20
        sc.blit(airship.image, airship.rect)
        # pygame.draw.rect(sc, (255, 255, 255), pygame.Rect(airship), 1)
        clock.tick(FPS)
        if airship_mask.overlap_area(obstruction_mask, (obstruction.rect.x - airship.rect.x, obstruction.rect.y - airship.rect.y)) > 0 or airship_mask.overlap_area(obstruction_mask2, (obstruction2.rect.x - airship.rect.x, obstruction2.rect.y - airship.rect.y)) > 0:
            print('пересечение')
    # else:
    #     sc.blit(button_play.image, button_play.rect)
    #     sc.blit(text_play, (370, 140))
    #     sc.blit(text_title, (270, 50))
        pygame.display.update()
