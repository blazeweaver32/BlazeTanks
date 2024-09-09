import pygame

from data.constants import objects, result_false, buttons
from data.images_load import imgMainMenu
from game_objects.button_logic import Button
from other_logic.json_logic import read_json


class UI:
    def __init__(self):
        pass


    def update(self):
        pass

    def draw(self):
        from run import window, fontUI, fontUITitle, fontUIPreTitle
        title_game = fontUI.render("BLAZE TANKS", 1, "white")
        rect_2 = title_game.get_rect(center=(400, 5 + 11))
        window.blit(title_game, rect_2)

        result = read_json("data/const.json")
        game_start = result['game_start']


        if game_start == "True" or game_start == "Again": #Game_UI or menu AgainPlay
            i = 0
            #Отображение победителя игры
            if len(result_false) != 0:
                for char in result_false:
                    text = fontUI.render(f"{char.nickname} проиграл", 1, char.color)
                    rect = text.get_rect(center = (400,280))
                    window.blit(text, rect)

                for obj in objects:
                    if obj.type == 'tank':
                        text = fontUI.render(f"{obj.nickname} выиграл", 1, obj.color)
                        rect = text.get_rect(center=(400, 300))
                        window.blit(text, rect)

                Button("blue", 400, 335, 130, 30, "Играть снова", "white", "game_again"),
                Button("red", 360, 335, 130, 30, "Выход", "white", "game_exit")

            else:
                for obj in objects:
                    if obj.type == 'tank':
                        if i == 0:
                            text_player = f"{obj.nickname} {str(obj.hp)}"
                        else:
                            text_player = f"{str(obj.hp)} {obj.nickname}"
                        text = fontUI.render(text_player, 1, obj.color)
                        rect = text.get_rect(center = (70 + i * 650, 5 + 11))
                        window.blit(text, rect)
                        i += 1

        elif game_start == "Options": #Options
            window.blit(imgMainMenu, (0, 0))

            option_name = fontUITitle.render("Настройки", 1, "white")
            rect_2 = option_name.get_rect(center=(400, 100))
            window.blit(option_name, rect_2)

            Button("red", 485, 50, 300, 30, "Поменять название игрока 1", "white", "сhange_nickname:first_player"),
            Button("blue", 485, 450, 300, 30, "Поменять название игрока 2", "white", "change_nickname:second_player"),

        elif game_start == "ChangeNicknameFirstPlayer" or game_start == "ChangeNicknameSecondPlayer":
            window.blit(imgMainMenu, (0, 0))
            nickname_text = fontUIPreTitle.render("Представьте нового бойца на поле!", 1, "white")
            #Create_InputBox
            input_box = pygame.draw.rect(window, "white", (80, 150, 650, 50))


            if pygame.time.get_ticks() % 1000 < 250:
                black = pygame.draw.rect(window, "white", (85, 152, 3, 45))
            else:
                black = pygame.draw.rect(window, "black", (85, 152, 3, 45))


            rect_nickname_text = nickname_text.get_rect(center=(400, 100))
            window.blit(nickname_text, rect_nickname_text)
        elif game_start == "False": #Main_Menu
            Button("blue", 285, 335, 130, 30, "Начать игру", "white", "game_start"),
            Button("blue", 325, 335, 130, 30, "Настройки", "white", "options_open"),
            Button("red", 365, 335, 130, 30, "Выход", "white", "game_exit")


            window.blit(imgMainMenu, (0, 0))


        for button in buttons:
            button.update()
            button.draw()
