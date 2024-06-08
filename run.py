import pygame


from data.images_load import imgBackground
from data.constants import WIDTH, HEIGHT, FPS, bullets, objects, TILE, DIRECTS
from game_objects.create_objects import create


pygame.init() #Инициализация pygame

window = pygame.display.set_mode((WIDTH, HEIGHT)) #Определение окна программы
clock = pygame.time.Clock() #Объект для отслеживания времени

fontUI = pygame.font.Font(None, 30) #Загрузка шрифтов. None - шрифт по умолчанию, второй параметр -размер шрифта


class UI:
    def __init__(self):
        pass


    def update(self):
        pass

    def draw(self):
        right_text = fontUI.render("BLAZE TANKS", 1, "white")
        rect_2 = right_text.get_rect(center=(5 * 70 + 32, 5 + 11))
        window.blit(right_text, rect_2)
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))
                text = fontUI.render(str(obj.hp), 1, obj.color)
                rect = text.get_rect(center = (5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                i += 1


ui = UI()



play = True

while play:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()


    if not objects:
        create(keys)

    for bullet in bullets: bullet.update()
    for obj in objects: obj.update()

    ui.update()

    window.fill('black')

    window.blit(imgBackground, (0, 0))

    for bullet in bullets: bullet.draw()
    for obj in objects: obj.draw()

    ui.draw()


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()