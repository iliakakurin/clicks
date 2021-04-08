# создать экран
# создать класс кружка (или отметить, какие у него будут атрибуты/свойства/переменные)

# координаты X, Y; размер (R); экран; изображение (IMAGE); прямоугольник

# разместить один круг на экране
import pygame
import sys
from clicks_classes import *

pygame.init()
pygame.mixer.init()
W = 600
H = 400
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

counter = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FPS = 60


CARS = ('car1.png', 'car2.png', 'car3.png')
# для хранения готовых машин-поверхностей
CARS_SURF = []

for i in range(len(CARS)):
    CARS_SURF.append(
        pygame.image.load(CARS[i]).convert_alpha())
circles = pygame.sprite.Group()
circle = Circle(CARS_SURF, circles)
print(CARS_SURF[0].get_rect().w, CARS_SURF[0].get_rect().h)

pygame.display.update()
# главный цикл
while True:
    counter += 1
    if counter % 60 == 0:
        circle = Circle(CARS_SURF, circles)
    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                a, b = i.pos[0], i.pos[1]
                for elem in circles:
                    # dist = (a - elem.rect.x) ** 2 + (b - elem.rect.y) ** 2
                    # if dist <= elem.r ** 2:
                    #     elem.kill()
                    if elem.rect.x <= a <= elem.rect.x + elem.rect.w and elem.rect.y <= b <= elem.rect.y + elem.rect.h:
                        elem.kill()


    sc.fill(WHITE)
    circles.draw(sc)
    pygame.display.update()

# создать группу объектов
# считать координаты клика мышки
# если клик попадает в координаты объекта, удалить его
