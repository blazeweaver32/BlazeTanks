import pygame

from data.constants import WIDTH, HEIGHT, FPS, bullets, objects, result_false
from data.images_load import imgBackground
from game_objects import ui
from game_objects.create_objects import create
from other_logic.json_logic import read_json, edit_json

pygame.init() #Инициализация pygame

window = pygame.display.set_mode((WIDTH, HEIGHT)) #Определение окна программы
clock = pygame.time.Clock() #Объект для отслеживания времени

fontUI = pygame.font.Font(None, 30) #Загрузка шрифтов. None - шрифт по умолчанию, второй параметр -размер шрифта
fontUITitle = pygame.font.Font(None, 72) #Загрузка шрифтов. None - шрифт по умолчанию, второй параметр -размер шрифта
fontUIPreTitle = pygame.font.Font(None, 50) #Загрузка шрифтов. None - шрифт по умолчанию, второй параметр -размер шрифта




play = True
edit_json("data/const.json", "game_start", "False")

while play:
    try:
        result = read_json("data/const.json")
        game_start = result['game_start']

        event_pygame = pygame.event.get()
        for event in event_pygame:
            if event.type == pygame.QUIT or game_start == "Exit":
                play = False

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        window.blit(imgBackground, (0, 0))


        if game_start == "True" or game_start == "Again":
            if game_start == "Again":
                bullets.clear()
                objects.clear()
                result_false.clear()
                edit_json("data/const.json", "game_start", "True")

            if not objects:
                create()

            for bullet in bullets: bullet.update()
            for obj in objects: obj.update()

            ui.update()


            for bullet in bullets: bullet.draw()
            for obj in objects: obj.draw()

        ui.update()
        ui.draw()

        pygame.display.update()
        clock.tick(FPS)
    except pygame.error:
        print("Программа выдала ошибку")
        break
        #TODO обработать правильно ошибку при выключение программы




pygame.quit()