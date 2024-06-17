import pygame

from data.constants import WIDTH, HEIGHT, FPS, bullets, objects
from data.images_load import imgBackground
from game_objects import ui
from game_objects.create_objects import create

pygame.init() #Инициализация pygame

window = pygame.display.set_mode((WIDTH, HEIGHT)) #Определение окна программы
clock = pygame.time.Clock() #Объект для отслеживания времени

fontUI = pygame.font.Font(None, 30) #Загрузка шрифтов. None - шрифт по умолчанию, второй параметр -размер шрифта




play = True

while play:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if not objects:
            create()

        for bullet in bullets: bullet.update()
        for obj in objects: obj.update()

        ui.update()

        window.blit(imgBackground, (0, 0))

        for bullet in bullets: bullet.draw()
        for obj in objects: obj.draw()

        ui.draw()

        pygame.display.update()
        clock.tick(FPS)
    except pygame.error:
        print("Программа выдала ошибку")
        break
        #TODO обработать правильно ошибку при выключение программы




pygame.quit()