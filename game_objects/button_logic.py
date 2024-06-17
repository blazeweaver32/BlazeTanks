import pygame

from data.constants import buttons
from other_logic.json_logic import edit_json


class Button:
    def __init__(self, color, px,py, height, width, font_text, font_color, action):
        buttons.append(self)
        self.type = 'button'
        self.color = color
        self.px = px
        self.py = py
        self.height = height
        self.width = width
        self.font_text = font_text
        self.font_color = font_color
        self.action = action

    def update(self):
        from run import event_pygame
        s_px = self.height + self.px
        s_py = self.width + self.py
        for event in event_pygame:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.px <= pos[0] <= s_px and self.py <= pos[1] <= s_py:
                    if self.action == "game_start":
                        edit_json("data/const.json", "game_start", "True")
                    elif self.action == "game_again":
                        edit_json("data/const.json", "game_start", "Again")
                    elif self.action == "game_exit":
                        edit_json("data/const.json", "game_start", "Exit")
                    elif self.action == "options_open":
                        edit_json("data/const.json", "game_start", "Options")
                    buttons.clear()



    def draw(self):
            from run import window, fontUI

            pygame.draw.rect(window, self.color, (self.px, self.py, self.height, self.width))
            title_game = fontUI.render(self.font_text, 1, self.font_color)
            rect_2 = title_game.get_rect(center=((self.px+self.width+35), (self.height+self.py-115)))
            window.blit(title_game, rect_2)



