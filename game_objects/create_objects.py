from data.constants import WIDTH,HEIGHT, TILE, objects

from game_objects.tank_logic import Tank

import pygame
from random import randint

def create(keys):
    Tank(keys, 'blue', 100, 275, 0, (
                               pygame.K_a,
                               pygame.K_d,
                               pygame.K_w,
                               pygame.K_s,
                               pygame.K_SPACE))


    Tank(keys, 'red', 650, 275, 0, (
                               pygame.K_LEFT,
                               pygame.K_RIGHT,
                               pygame.K_UP,
                               pygame.K_DOWN,
                               pygame.K_f))


    for _ in range(50):
        while True:
            x = randint(0, WIDTH // TILE - 1) * TILE
            y = randint(1, HEIGHT // TILE - 1) * TILE

            rect = pygame.Rect(x, y, TILE, TILE)

            fined = False

            for obj in objects:
                if rect.colliderect(obj.rect): fined = True

            if not fined: break

        from game_objects.block_logic import Block
        Block(x, y, TILE)