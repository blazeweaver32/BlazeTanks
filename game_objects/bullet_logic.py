import pygame

from data.constants import WIDTH, HEIGHT, bullets, objects
from game_objects.bang_logic import Bang


class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)

        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.px, self.py, False)
                    break

    def draw(self):
        from run import window
        pygame.draw.circle(window, "yellow", (self.px, self.py), 2)

