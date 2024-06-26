import pygame

from data.constants import TILE, HEIGHT, WIDTH, DIRECTS, objects, result_false
from data.images_load import imgTanks
from game_objects.bang_logic import Bang
from game_objects.bullet_logic import Bullet


class Tank:
    def __init__(self, nickname, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.nickname = nickname
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 3
        self.hp = 5

        self.destroyed = False

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 7
        self.bulletDamage = 1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]


        if self.color == "red":
            self.imgTanksColor = imgTanks[0]
        elif self.color == "blue":
            self.imgTanksColor = imgTanks[1]

        self.image = pygame.transform.rotate(self.imgTanksColor, -self.direct * 90)
        self.rect = self.image.get_rect(center = self.rect.center)
    def update(self):
        from run import keys, mouse

        if self.color == "red":
            self.imgTanksColor = imgTanks[0]
        elif self.color == "blue":
            self.imgTanksColor = imgTanks[1]

        self.image = pygame.transform.rotate(self.imgTanksColor, -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() -5, self.image.get_height() -5))
        self.rect = self.image.get_rect(center = self.rect.center)

        oldx, oldy = self.rect.topleft

        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2


        if self.rect.y < 0:
            self.rect.y = HEIGHT
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH
        if self.rect.x > WIDTH:
            self.rect.x = 0


        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldx, oldy
        if self.keySHOT in [0, 1, 2]:
            shot_key = mouse[self.keySHOT]
        else:
            shot_key = keys[self.keySHOT]
        if shot_key and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)

            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1


    def draw(self):
        from run import window

        window.blit(self.image, self.rect)

        if self.destroyed:
            Bang(self.rect.centerx, self.rect.centery, True)
            result_false.append(self)
            objects.remove(self)

    def damage(self, value):
        self.hp -= value

        if self.hp <= 0:
            self.destroyed = True
