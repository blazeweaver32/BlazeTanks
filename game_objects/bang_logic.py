import pygame

from data.constants import objects
from data.images_load import imgBangs, imgBangsDestroyedTanks


class Bang:
    def __init__(self, px, py, destroyed):
        objects.append(self)
        self.type = 'bang'
        self.destroyed = destroyed

        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3: objects.remove(self)

    def draw(self):
        if self.destroyed:
            image = imgBangsDestroyedTanks[int(self.frame)]
            image = pygame.transform.scale(image, (image.get_width() + 15, image.get_height() + 15))
        else:
            image = imgBangs[int(self.frame)]
        rect = image.get_rect(center = (self.px, self.py))

        from run import window
        window.blit(image, rect)