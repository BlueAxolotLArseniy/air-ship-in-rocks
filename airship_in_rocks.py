import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

ComplexitY = 50


def random_holst(hol, y, draw):
    global ComplexitY
    x = 0
    if draw == 'up':
        pygame.draw.polygon(hol, (0, 0, 0), [[0, 0],
                                                    [0, y],
                                                    [x+100, random.randint(y-ComplexitY, y+ComplexitY)],
                                                    [x+200, random.randint(y-ComplexitY, y+ComplexitY)],
                                                    [x+300, random.randint(y-ComplexitY, y+ComplexitY)],
                                                    [x+400, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+500, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+600, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+700, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+800, y],
                                                    [800, 0]])
    if draw == 'down':
        pygame.draw.polygon(hol, (0, 0, 0), [[0, 500],
                                                    [0, y],
                                                    [x+100, random.randint(y-ComplexitY, y+ComplexitY)],
                                                    [x+200, random.randint(y-ComplexitY, y+ComplexitY)],
                                                    [x+300, random.randint(y-ComplexitY, y+ComplexitY)],
                                                    [x+400, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+500, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+600, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+700, random.randint(y - ComplexitY, y + ComplexitY)],
                                                    [x+800, y],
                                                    [800, 500]])

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

f1 = pygame.font.Font(None, 36)
text_title = f1.render('AIRSHIP_IN_IN_ROCKS', True, (255, 255, 255))
text_play = f1.render('PLAY', True, (255, 255, 255))


button_play = Buttons_in_menu(400, 150, 'Button.png')
obstruction = ObstrucTion(800*3/2, 250, 'obstruction_texture56.png')
obstruction_mask = pygame.mask.from_surface(obstruction.image)
obstruction2 = ObstrucTion(800*3/2+2400, 250, 'obstruction_texture56.png')
obstruction_mask2 = pygame.mask.from_surface(obstruction2.image)

holst = pygame.Surface((800, 500), pygame.SRCALPHA, 32) # Прозрачность фона
game_holst = pygame.Surface((800, 500), pygame.SRCALPHA, 32) # Прозрачность фона
holst = holst.convert_alpha() # Прозрачность фона
game_holst = game_holst.convert_alpha() # Прозрачность фона

random_holst(holst, 100, 'up')
random_holst(holst, 380, 'down')
random_holst(game_holst, 380, 'down')
random_holst(game_holst, 100, 'up')

sc.blit(holst, (400,200))
holst_rect = holst.get_rect()
holst_rect.x = 0
holst_rect.y = 0
game_holst_rect = game_holst.get_rect()
game_holst_rect.x = 800
game_holst_rect.y = 0

mask1 = pygame.mask.from_surface(holst)
game_mask = pygame.mask.from_surface(game_holst)

clock = pygame.time.Clock()
FPS = 30

r = random.randint(1, 3)

def reset_holst(hol):
    global game_holst, holst
    if hol == 'gameholst':
        game_holst = None
        game_holst = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
        random_holst(game_holst, 380, 'down')
        random_holst(game_holst, 100, 'up')
    if hol == 'holst':
        holst = None
        holst = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
        random_holst(holst, 380, 'down')
        random_holst(holst, 100, 'up')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    sc.fill((30, 30, 30))

    # if menu == False:
    speed_fall()
    touch()

    smoothness_rotate()

    if game_holst_rect.x <= -800:
        reset_holst('gameholst')
        game_holst_rect.x = 800
    if holst_rect.x <= -800:
        reset_holst('holst')
        holst_rect.x = 800

    holst_rect.x -= 10
    sc.blit(holst, (holst_rect.x, holst_rect.y))
    game_holst_rect.x -= 10
    sc.blit(game_holst, (game_holst_rect.x, game_holst_rect.y))

    # if obstruction.rect.right < 10:
    #     obstruction.rect.left = obstruction2.rect.right
    #     if random.randint(1, 2) == 2:
    #         obstruction.cheange_image("obstruction_texture57.png")
    #     else:
    #         obstruction.cheange_image("obstruction_texture56.png")
    # if obstruction2.rect.right < 10:
    #     obstruction2.rect.left = obstruction.rect.right
    #     if random.randint(1, 2) == 2:
    #         obstruction2.cheange_image("obstruction_texture57.png")
    #     else:
    #         obstruction2.cheange_image("obstruction_texture56.png")



    # sc.blit(obstruction.image, obstruction.rect)
    # sc.blit(obstruction2.image, obstruction2.rect)
    # obstruction.rect.x -= 20
    # obstruction2.rect.x -= 20
    sc.blit(airship.image, airship.rect)
    pygame.draw.rect(sc, (255, 255, 255), pygame.Rect(airship), 1)
    clock.tick(FPS)
    # if airship_mask.overlap_area(obstruction_mask, (obstruction.rect.x - airship.rect.x, obstruction.rect.y - airship.rect.y)) > 0 or airship_mask.overlap_area(obstruction_mask2, (obstruction2.rect.x - airship.rect.x, obstruction2.rect.y - airship.rect.y)) > 0:
    #     print('пересечение')
    offset = (int(airship.rect.x - holst_rect.x), int(airship.rect.y - holst_rect.y))
    if mask1.overlap_area(airship_mask, offset):
        print('пересечение')
    offset = (int(airship.rect.x - game_holst_rect.x), int(airship.rect.y - game_holst_rect.y))
    if game_mask.overlap_area(airship_mask, offset):
        print('пересечение')
    pygame.display.update()
