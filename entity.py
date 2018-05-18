# -*- coding:utf8 -*-
import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

TYPE_SMALL = 1
TYPE_MIDDLE = 2
TYPE_BIG = 3


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_img = bullet_img
        self.rect = self.bullet_img.get_rect()
        self.speed = 10
        self.rect.midbottom = init_pos

    def move(self):
        self.rect.top -= self.speed


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_img = bullet_img
        self.rect = self.bullet_img.get_rect()
        self.speed = 10
        self.rect.midtop = init_pos

    def move(self):
        self.rect.top += self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.img = []
        for item in player_rect:
            self.img.append(player_img.subsurface(item).convert_alpha())
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        self.bullets = pygame.sprite.Group()
        self.speed = 8
        self.img_index = 0
        self.is_hit = False

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img=bullet_img, init_pos=self.rect.midtop)
        self.bullets.add(bullet)

    def move_up(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def move_down(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def move_left(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def move_right(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = down_imgs
        self.speed = 5
        self.down_index = 0
        self.bullets = pygame.sprite.Group()

    def move(self):
        self.rect.top += self.speed

    def attack(self, bullet_img):
        bullet = EnemyBullet(bullet_img=bullet_img, init_pos=self.rect.midbottom)
        self.bullets.add(bullet)


