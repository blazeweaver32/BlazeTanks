import pygame

from data.images_load import imgBrick
from data.constants import objects



class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        from run import window
        window.blit(imgBrick, self.rect)
        pygame.draw.rect(window, "gray20", self.rect, 2)
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: objects.remove(self)
