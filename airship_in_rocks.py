import sys
import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pygame.display.set_caption('airship in rocks')

ComplexitY = 30

pause = True

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

airship = AirShip(50, 200, 'airship_texture.png')
airship_mask = pygame.mask.from_surface(airship.image)
airship_y = 0
direction = 0
gravitation = 0
number_gravitation = 1
rotate = 1
MOVE_OBSTRUCTIONS = 30
point = 0

obs1 = ObstrucTion(0, 0, 'obs.png')
obs2 = ObstrucTion(2400, 0, 'obs.png')

obs11 = ObstrucTion(0, 0, 'obs2.png')
obs22 = ObstrucTion(2400, 0, 'obs2.png')

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

f1 = pygame.font.Font(None, 36)
text1 = f1.render('q = quit   p = play   esc = menu', True,
                  (255, 255, 0))
text2 = f1.render('AIRSHIP IN ROCKS', True,
                  (255, 255, 255))

whilee = False
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            whilee = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = False
            elif event.key == pygame.K_ESCAPE:
                pause = True
            elif event.key == pygame.K_q:
                whilee = True
    sc.fill((50, 50, 50))
    if pause == True:
        sc.blit(text1, (230, 250))
        sc.blit(text2, (290, 100))
        pygame.display.update()
    if whilee == True: break
    if pause == False:


        obs11.rect.x -= 2
        obs22.rect.x -= 2
        obs11.rect.y = 0
        obs22.rect.y = 0

        if obs11.rect.x <= -2400:
            obs11.rect.x = 2400
        if obs22.rect.x <= -2400:
            obs22.rect.x = 2400

        sc.blit(obs11.image, obs11.rect)
        sc.blit(obs22.image, obs22.rect)

        obs1.rect.x -= 4
        obs2.rect.x -= 4
        obs1.rect.y = 0
        obs2.rect.y = 0

        if obs1.rect.x <= -2400:
            obs1.rect.x = 2400
        if obs2.rect.x <= -2400:
            obs2.rect.x = 2400

        sc.blit(obs1.image, obs1.rect)
        sc.blit(obs2.image, obs2.rect)

        point += 1
        speed_fall()
        touch()

        if point % 12 == 0:
            ComplexitY += 1

        smoothness_rotate()

        if game_holst_rect.x <= -800:
            reset_holst('gameholst')
            game_holst_rect.x = 800
        if holst_rect.x <= -800:
            reset_holst('holst')
            holst_rect.x = 800

        holst_rect.x -= 20
        sc.blit(holst, (holst_rect.x, holst_rect.y))
        game_holst_rect.x -= 20
        sc.blit(game_holst, (game_holst_rect.x, game_holst_rect.y))

        sc.blit(airship.image, airship.rect)
        # pygame.draw.rect(sc, (255, 255, 255), pygame.Rect(airship), 1)
        clock.tick(FPS)

        if point > 150:
            offset = (int(airship.rect.x - holst_rect.x), int(airship.rect.y - holst_rect.y))
            if mask1.overlap_area(airship_mask, offset):
                print('пересечение')
                break
            offset = (int(airship.rect.x - game_holst_rect.x), int(airship.rect.y - game_holst_rect.y))
            if game_mask.overlap_area(airship_mask, offset):
                print('пересечение')
                break
        if whilee == True: break
        pygame.display.update()

pygame.quit()
sys.exit()