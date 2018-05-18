# -*- coding:utf8 -*-

import pygame
from random import randint
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_images, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_index = 0
        self.imgs = enemy_images
        self.img = self.imgs[0]
        self.rect = self.img.get_rect()
        self.rect.topleft = init_pos
        self.speed = 4
        self.attack_frequence = 0
        self.down_frequence = 0
        self.enemy_bullets = pygame.sprite.Group()
        self.health = 6
        self.is_killed = False
        self.is_strong = False

    def move(self):
        self.rect.top += self.speed

    def attcak(self, enemy_bullet_imgs, mid=False):
        if mid:
            init_pos = self.rect.midbottom
        else:
            init_pos = [self.rect.left + 10, self.rect.bottom - 5]
        enemy_bullet = EnemyBullet(imgs=enemy_bullet_imgs, init_pos=init_pos)
        self.enemy_bullets.add(enemy_bullet)


class Prop(pygame.sprite.Sprite):
    def __init__(self, imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_index = 0
        self.imgs = imgs
        self.img = self.imgs[0]
        self.rect = self.img.get_rect()
        self.rect.topleft = init_pos
        self.speed = 4
        self.eye_frequence = 0
        self.enemy_bullets = pygame.sprite.Group()
        self.health = 50

    def move(self):
        self.rect.top += self.speed


class Mon(Enemy):
    def __init__(self, imgs, init_pos):
        Enemy.__init__(self, imgs, init_pos)
        self.health = 70
        self.power = 50
        self.should_show = False
        self.play = False
        self.final_show = False
        self.final_attack = False
        self.speed = 5
        self.mon_bullets = pygame.sprite.Group()

    def move_down(self):
        if abs(self.rect.top) > self.img.get_rect().height / 2.0:
            self.rect.top += self.speed
        else:
            self.play = True

    def move_up(self):
        if not self.should_show:
            if abs(self.rect.top) < self.img.get_rect().height:
                self.rect.top -= self.speed

    def final_move(self):
        if self.rect.top < 0:
            self.rect.top += self.speed
        else:
            self.final_attack = True

    def show(self):
        if self.should_show:
            self.move_down()

    def attack(self, mon_bullet_imgs):
        if self.health > 50:
            b1 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b2 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b2.move_mode = "center_left"
            b3 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b3.move_mode = "center_right"
            self.mon_bullets.add(b1)
            self.mon_bullets.add(b2)
            self.mon_bullets.add(b3)
        else:
            b1 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b2 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b2.move_mode = "center_left"
            b3 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b3.move_mode = "center_right"
            self.mon_bullets.add(b1)
            self.mon_bullets.add(b2)
            self.mon_bullets.add(b3)
            b4 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b5 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b5.move_mode = "center_left"
            b6 = MonBullet(imgs=mon_bullet_imgs, init_pos=self.rect.midbottom)
            b6.move_mode = "center_right"
            init_speed = b4.speed * 2
            b4.speed = b5.speed = b6.speed = init_speed
            self.mon_bullets.add(b4)
            self.mon_bullets.add(b5)
            self.mon_bullets.add(b6)



class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = imgs
        self.img = imgs[0]
        self.rect = self.img.get_rect()
        self.speed = 5
        self.rect.midtop = init_pos
        self.frequence = 0

    def move(self):
        self.rect.top += self.speed


class MonBullet(EnemyBullet):
    def __init__(self, imgs, init_pos):
        EnemyBullet.__init__(self, imgs, init_pos)
        self.move_mode = "center"

    def move(self, mode="center"):
        if self.move_mode == "center":
            self.rect.top += self.speed
        if self.move_mode == "center_left":
            self.rect.top += self.speed
            self.rect.left -= self.speed // randint(1, 3)
        if self.move_mode == "center_right":
            self.rect.top += self.speed
            self.rect.right += self.speed // randint(1, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_img = bullet_img
        self.rect = self.bullet_img.get_rect()
        self.speed = 10
        self.rect.midbottom = init_pos

    def move(self):
        self.rect.top -= self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self, player_images, init_pos=[0, 0]):
        self.img_index = 0
        self.imgs = player_images
        self.shanxian = False
        self.shanxian_frequence = 0
        self.img = player_images[0]
        self.rect = self.img.get_rect()
        self.rect.topleft = init_pos
        self.speed = 8
        self.is_killed = False
        self.health = 200.0
        self.great_health = 200.0
        self.bullets = pygame.sprite.Group()
        # 攻击力是3
        self.power = 3

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

    def fresh_health(self, surface):
        bar_x = self.rect.left
        bar_y = self.rect.bottom + 10
        bar_width = self.img.get_rect().width
        bar_height = 4
        # blood_img = pygame.image.load('./resources/image/player/blood/blood_01.png')
        # blood_img.rect.topleft = [bar_x, bar_y]
        #surface.blit(blood_img, (bar_x, bar_y))
        if self.health > self.great_health:
            self.health = self.great_health
        surface.fill((255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        now_bar_width = (self.health / self.great_health) * bar_width
        surface.fill((0, 255, 0), (bar_x, bar_y, now_bar_width, bar_height))

