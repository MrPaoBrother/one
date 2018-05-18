# -*- coding:utf8 -*-

import pygame
import time
from sys import exit
from pygame.locals import *
from models import *
import random
from random import randint


# 初始化游戏
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('one作战')

bac_img = pygame.image.load('./resources/image/background.png')

"""
player
"""
player_images = []
player_up = pygame.image.load('./resources/image/player/nom_action/nom_up_01.png')
player_down = pygame.image.load('./resources/image/player/nom_action/nom_down_06.png')
player_left = pygame.image.load('./resources/image/player/nom_action/nom_left_03.png')
player_right = pygame.image.load('./resources/image/player/nom_action/nom_right_05.png')
player_dead = pygame.image.load('./resources/image/player/nom_action/nom_die.png')
player_images.append(player_up)
player_images.append(player_down)
player_images.append(player_left)
player_images.append(player_right)
player_images.append(player_dead)
# 之所以这个位置 是给英雄出场一个动画效果，飞翔出来
init_pos = [SCREEN_WIDTH / 2 - player_up.get_rect().width / 2, 600]
player = Player(player_images=player_images, init_pos=init_pos)

"""
bullet
"""
bullet_img = pygame.image.load('./resources/image/player/nom_attack/nom_attack_up.png')

mon_bullet_imgs = []
mon_bullet_imgs.append(pygame.image.load('./resources/image/bullet/bullet_big.png'))

"""
enemy
"""
# 定义敌机对象使用的surface相关参数
player_img = pygame.image.load('./resources/image/shoot.png')

# bullet_rect = pygame.Rect(1004, 987, 9, 21)
# enemy_bullet_img = player_img.subsurface(bullet_rect)
enemy_bullet_imgs = []
enemy_bullet_img = pygame.image.load('./resources/image/bullet/bullet_small_01.png')
enemy_bullet_imgs.append(pygame.image.load('./resources/image/bullet/bullet_small_left.png'))
enemy_bullet_imgs.append(pygame.image.load('./resources/image/bullet/bullet_small_right.png'))

enemy_strong_bullets = []
enemy_strong_bullets.append(pygame.image.load('./resources/image/bullet/bullet_middle.png'))
"""
敌人组
"""
enemy_imgs = []
enemy1_imgs = []
enemy1_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_01_1.png'))
enemy1_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_01_2.png'))

enemy2_imgs = []
enemy2_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_02_1.png'))
enemy2_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_02_2.png'))

"""
enemy3_imgs = []
enemy3_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_03_1.png'))
enemy3_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_03_2.png'))
"""
enemy4_imgs = []
enemy4_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_04_1.png'))
enemy4_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_04_2.png'))

enemy5_imgs = []
enemy5_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_05_1.png'))
enemy5_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_05_2.png'))
"""
enemy6_imgs = []
enemy6_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_06_1.png'))
enemy6_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_06_2.png'))
"""
enemy7_imgs = []
enemy7_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_07_1.png'))
enemy7_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_07_2.png'))
enemy8_imgs = []
enemy8_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_08_1.png'))
enemy8_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_08_2.png'))
enemy9_imgs = []
enemy9_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_09_1.png'))
enemy9_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_09_2.png'))
enemy10_imgs = []
enemy10_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_10_1.png'))
enemy10_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_10_2.png'))
enemy11_imgs = []
enemy11_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_11_1.png'))
enemy11_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_11_2.png'))
enemy12_imgs = []
enemy12_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_12_1.png'))
enemy12_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_12_2.png'))
enemy13_imgs = []
enemy13_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_13_1.png'))
enemy13_imgs.append(pygame.image.load('./resources/image/enemy/smo_act/smo_13_2.png'))

enemy_strong_imgs = []
enemy_strong_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_01.png'))
enemy_strong_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_02.png'))

enemy_imgs.append(enemy1_imgs)
enemy_imgs.append(enemy2_imgs)
# enemy_imgs.append(enemy3_imgs)
enemy_imgs.append(enemy4_imgs)
enemy_imgs.append(enemy5_imgs)
# enemy_imgs.append(enemy6_imgs)
enemy_imgs.append(enemy7_imgs)
enemy_imgs.append(enemy8_imgs)
enemy_imgs.append(enemy9_imgs)
enemy_imgs.append(enemy10_imgs)
enemy_imgs.append(enemy11_imgs)
enemy_imgs.append(enemy12_imgs)
enemy_imgs.append(enemy13_imgs)
enemy_imgs.append(enemy_strong_imgs)

enemy1_hit_imgs = []
enemy1_hit_imgs.append(pygame.image.load('./resources/image/enemy/smo_hit/smo_hit_01-1.png'))
enemy1_hit_imgs.append(pygame.image.load('./resources/image/enemy/smo_hit/smo_hit_01_2.png'))

enemy1_down_imgs = []
enemy1_down_imgs.append(pygame.image.load('./resources/image/enemy/smo_dead/smo_dead_01_1.png'))
enemy1_down_imgs.append(pygame.image.load('./resources/image/enemy/smo_dead/smo_dead_01_2.png'))
enemy1_down_imgs.append(pygame.image.load('./resources/image/enemy/smo_dead/smo_dead_02_1.png'))
enemy1_down_imgs.append(pygame.image.load('./resources/image/enemy/smo_dead/smo_dead_02_2.png'))

enemy_cro_imgs = []
enemy_cro_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_01.png'))
enemy_cro_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_02.png'))
enemy_cro_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_anger_01.png'))
enemy_cro_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_anger_02.png'))
enemy_cro_imgs.append(pygame.image.load('./resources/image/enemy/cro/cro_dead.png'))

mon_images = []
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_01.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_02.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_03.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_04.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_05.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_06.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_07.png'))
mon_images.append(pygame.image.load('./resources/image/enemy/mon/mon_08.png'))
mon = Mon(imgs=mon_images, init_pos=(0, -mon_images[0].get_rect().height))

mon_anger_6 = pygame.image.load('./resources/image/enemy/mon/mon_anger_01.png')
mon_anger_3= pygame.image.load('./resources/image/enemy/mon/mon_anger_01.png')

bac_images = []
bac_images.append(pygame.image.load('./resources/image/bac/bc_1.png'))
bac_images.append(pygame.image.load('./resources/image/bac/bc_2.png'))
bac_images.append(pygame.image.load('./resources/image/bac/bc_3.png'))
bac_images.append(pygame.image.load('./resources/image/bac/bc_4.png'))

props_images = []
props_images.append(pygame.image.load('./resources/image/props/Cur.png'))
props_images.append(pygame.image.load('./resources/image/props/Cur_2.png'))

clock = pygame.time.Clock()

bullet_sound = pygame.mixer.Sound('./resources/sound/bullet.wav')
bullet_sound.set_volume(0.3)

enemy_shoot_sound = pygame.mixer.Sound('./resources/sound/enemy_shoot.ogg')
enemy_shoot_sound.set_volume(0.3)

enemy1_down_sound = pygame.mixer.Sound('./resources/sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.3)
enemy1_down_sound = pygame.mixer.Sound('resources/sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.3)

enemy1_dead_sound = pygame.mixer.Sound('resources/sound/enemy1_dead.wav')
enemy1_dead_sound.set_volume(0.25)

player_win_sound = pygame.mixer.Sound('resources/sound/win.ogg')
player_win_sound.set_volume(0.25)

player_shoot = pygame.mixer.Sound('./resources/music/player_shoot.wav')
player_shoot.set_volume(0.3)

mon_shoot = pygame.mixer.Sound('./resources/sound/mon_shoot.wav')
mon_shoot.set_volume(0.3)
game_over_sound = pygame.mixer.Sound('resources/sound/game_over.ogg')
game_over_sound.set_volume(0.3)

pygame.mixer.music.load('./resources/sound/bac_1.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


def do_action(key_presses, obj, action_name="", frequence=0):
    if action_name == "player_move":
        if key_presses[K_UP]:
            obj.img = player_up
            obj.move_up()
        if key_presses[K_DOWN]:
            obj.img = player_down
            obj.move_down()
        if key_presses[K_LEFT]:
            obj.img = player_left
            obj.move_left()
        if key_presses[K_RIGHT]:
            obj.img = player_right
            obj.move_right()

        if key_presses[K_RIGHT] and key_presses[K_SPACE]:
            # 闪现
            x, y = obj.rect.topright
            to_place = x + 30
            x = to_place if to_place < SCREEN_WIDTH else SCREEN_WIDTH
            obj.rect.topright = [x, y]
            screen.blit(obj.img, [x, y])

    if action_name == "player_shoot":
        if key_presses[K_x]:
            player.shoot(bullet_img=bullet_img)

is_shoot = False

enemy_group = pygame.sprite.Group()
enemy_hit_group = pygame.sprite.Group()
enemy_down_group = pygame.sprite.Group()
prop_group = pygame.sprite.Group()

bac_y = 800
which_bac = 0

shoot_frequence = 0
enemy_show_frequence = 0
enemy_strong_show_frequence = 1
enemy_action_frequence = 0
enemy_down_frequence = 0

prop_show_frequence = 0

mon_frequence = 0
mon_show_frequence = 0
mon_final_attack_frequence = 0
mon_dead_frequence = 0
player_killed_frequence = 0
game_continue = True

lose = True
# 打怪赚的积分
score = 0
import time
start_time = time.time()
while game_continue:
    clock.tick(60)
    fresh_bac = bac_images[which_bac].subsurface(pygame.Rect(0, bac_y, 480, 800))
    screen.blit(fresh_bac, (0, 0))
    # 背景移动
    bac_y -= 2
    if bac_y <= 0:
        which_bac = which_bac+1 if which_bac < 3 else 0
        bac_y = 800

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # 键盘按键
    key_presses = pygame.key.get_pressed()
    if key_presses[K_q]:
        exit()
    do_action(key_presses, player, action_name="player_move")
    if key_presses[K_x]:
        is_shoot = True

    if enemy_show_frequence % 80 == 0:
        # 随机创建一个小怪图像组
        rand_num = randint(-1, 10)
        rand_enemy_imgs = enemy_imgs[rand_num]
        random_pos = [randint(0, SCREEN_WIDTH - rand_enemy_imgs[0].get_rect().width), 0]
        enemy = Enemy(rand_enemy_imgs, random_pos)
        if rand_num == -1:
            enemy.is_strong = True
        enemy_group.add(enemy)
        # enemy.attcak(enemy_bullet_img=enemy_bullet_img)
    if enemy_show_frequence > 200:
        enemy_show_frequence = 0
    enemy_show_frequence += 1

    if prop_show_frequence % 200 == 0:
        prop_pos = [randint(0, SCREEN_WIDTH - props_images[0].get_rect().width), 0]
        prop = Prop(imgs=props_images, init_pos=prop_pos)
        prop_group.add(prop)
    if prop_show_frequence > 600:
        prop_show_frequence = 0
    prop_show_frequence += 1

    if is_shoot:
        shoot_frequence += 1
        if shoot_frequence % 8 == 0:
            player_shoot.play()
            player.shoot(bullet_img)
            is_shoot = False
            shoot_frequence = 0

    if player.is_killed:
        player.img = player.imgs[-1]
    # enemy_downs = pygame.sprite.groupcollide(enemy_group, player.bullets, 1, 1)

    enemy_hits = pygame.sprite.groupcollide(enemy_group, player.bullets, 0, 1)
    for enemy in enemy_hits:
        enemy.health -= player.power
        if enemy.health <= 0:
            enemy.is_killed = True
            score += 1000
            enemy_group.remove(enemy)
            enemy_down_group.add(enemy)
            continue
        enemy.imgs = enemy1_hit_imgs

    for prop in prop_group:
        if prop.eye_frequence % 30 == 0:
            prop.image_index = 0 if prop.image_index == 1 else 1
        prop.eye_frequence += 1
        if prop.eye_frequence > 90:
            prop.eye_frequence = 0
        screen.blit(prop.imgs[prop.image_index], prop.rect)
        prop.move()
        if pygame.sprite.collide_circle(prop, player):
            player.health += prop.health
            score += 2000
            prop_group.remove(prop)
        if prop.rect.top > SCREEN_HEIGHT:
            prop_group.remove(prop)

    for enemy in enemy_group:
        if enemy.attack_frequence % 50 == 0:
            if enemy.image_index == 0:
                enemy.image_index = 1
                if enemy.is_strong:
                    enemy.attcak(enemy_strong_bullets)
                    enemy_shoot_sound.play()
                else:
                    enemy.attcak(enemy_bullet_imgs)
            else:
                enemy.image_index = 0
            enemy.img = enemy.imgs[enemy.image_index]
        if pygame.sprite.collide_circle(enemy, player):
            player.health -= 2
            if player.health <= 0:
                player.is_killed = True
            enemy_down_group.add(enemy)
            enemy_group.remove(enemy)

        enemy.attack_frequence += 1
        if enemy.attack_frequence > 100:
            enemy.attack_frequence = 0
        screen.blit(enemy.img, enemy.rect)
        enemy.move()
        if enemy.rect.top > SCREEN_HEIGHT:
            enemy_group.remove(enemy)

    for enemy_down in enemy_down_group:
        enemy_down.imgs = enemy1_down_imgs
        if enemy_down.down_frequence > 37:

            enemy_down_group.remove(enemy_down)
            continue
        screen.blit(enemy_down.imgs[enemy_down.down_frequence // 19], enemy_down.rect)
        enemy_down.speed = 6
        enemy_down.move()
        enemy_down.down_frequence += 1

    for enemy in enemy_group:
        for enemy_bullet in enemy.enemy_bullets:
            if enemy.is_strong:
                enemy_bullet.img = enemy_bullet_imgs[enemy_bullet.frequence // 20]
            else:
                enemy_bullet.img = enemy_bullet_imgs[enemy_bullet.frequence // 10]
            screen.blit(enemy_bullet.img, enemy_bullet.rect)
            enemy_bullet.frequence += 1
            if enemy_bullet.frequence >= 20:
                enemy_bullet.frequence = 0
            enemy_bullet.move()
            if pygame.sprite.collide_circle(enemy_bullet, player):
                player.health -= 1
                enemy.enemy_bullets.remove(enemy_bullet)
                if player.health <= 0:
                    player.is_killed = True
            if enemy_bullet.rect.top > SCREEN_HEIGHT:
                enemy.enemy_bullets.remove(enemy_bullet)
    player.fresh_health(screen)
    screen.blit(player.img, player.rect)

    if player.is_killed:
        game_over_sound.play()
        if player_killed_frequence // 2 == 2:
            lose = True
            break
        player_killed_frequence += 1

    # 老怪动画
    if not mon.should_show:
        mon.move_up()
        if randint(0, 80) == 0:
            mon.should_show = True
    if mon.should_show and not mon.final_show:
        mon.move_down()
        if mon.play:
            mon.img = mon.imgs[mon_frequence // 8]
            screen.blit(mon.img, mon.rect)
            mon_frequence += 1
            if mon_frequence == 50:
                mon.attack(mon_bullet_imgs)
            if mon_frequence >= 56:
                mon_frequence = 0
                mon.should_show = False
                mon.play = False
    for mon_bullet in mon.mon_bullets:
        screen.blit(mon_bullet.img, mon_bullet.rect)
        mon_bullet.move()
        if mon_bullet.rect.top > SCREEN_HEIGHT or mon_bullet.rect.left < 0 or mon_bullet.rect.right > SCREEN_WIDTH:
            mon.mon_bullets.remove(mon_bullet)
        if pygame.sprite.collide_circle(mon_bullet, player):
            player.health -= mon.power
            mon.mon_bullets.remove(mon_bullet)
    # 10000分老怪出现
    if not mon.final_show and score >= 10000:
        pygame.mixer.music.load('./resources/sound/mon_load.ogg')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.25)
        print "final show!!!!!"
        mon.final_show = True
    if mon.final_show:
        mon.final_move()
    if mon.final_attack:
        mon_remain_health = mon.health
        health_font = pygame.font.Font(None, 40)
        health_font = health_font.render(str("HP:"+str(mon_remain_health)), True, (240, 0, 0))
        health_font_rect = health_font.get_rect()
        health_font_rect.topleft = [10, 60]
        screen.blit(health_font, health_font_rect)
        if mon.health <= 50:
            mon.imgs[6] = mon_anger_6
            mon.imgs[3] = mon_anger_3
        mon.img = mon.imgs[mon_final_attack_frequence // 8]
        screen.blit(mon.img, mon.rect)
        mon_final_attack_frequence += 1

        if mon_final_attack_frequence == 50:
            mon.attack(mon_bullet_imgs)
        if mon_final_attack_frequence >= 56:
            mon_final_attack_frequence = 0
        for bullet in player.bullets:
            if pygame.sprite.collide_circle(bullet, mon):
                mon.health -= player.power
                player.bullets.remove(bullet)
                if mon.health <= 0:
                    mon.is_killed = True
                    lose = False
    if mon.is_killed:
        if mon_dead_frequence // 2 == 3:
            player_win_sound.play()
            # 这里应该有一段老怪死亡动画
            break
        mon_dead_frequence += 1

    for bullet in player.bullets:
        screen.blit(bullet.bullet_img, bullet.rect)
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)
    # 绘制得分
    score_font = pygame.font.Font(None, 36)
    score_font = score_font.render(str(score), True, (240, 0, 0))
    text_rect = score_font.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_font, text_rect)

    if 7000 <= score <= 10000:
        tip_font = pygame.font.Font(None, 40)
        tip_font = tip_font.render(str("Mon is already out!!!"), True, (240, 0, 0))
        tip_font_rect = score_font.get_rect()
        tip_font_rect.topleft = [10, 50]
        screen.blit(tip_font, tip_font_rect)

    pygame.display.update()

end_time = time.time()
all_time = end_time - start_time

game_over_bac = pygame.image.load('./resources/image/bac/bc_end.png')
game_vitory = pygame.image.load('./resources/image/bac/bc_win.png')

game_word = "Game Over" if lose else "Vitory!"
game_bac = game_over_bac if lose else game_vitory

game_over_font = pygame.font.Font(None, 100).render(game_word, True, (255, 0, 0))
game_over_rect = game_over_font.get_rect()
game_over_rect.centerx = SCREEN_WIDTH / 2
game_over_rect.centery = 100


final_score = pygame.font.Font(None, 64).render("Score: "+str(score), True, (255, 0, 0))
final_score_rect = final_score.get_rect()
final_score_rect.centerx = SCREEN_WIDTH / 2
final_score_rect.centery = 200

final_time = pygame.font.Font(None, 64).render(str('Time: %.2f' % all_time), True, (255, 0, 0))
final_time_rect = final_score.get_rect()
final_time_rect.centerx = SCREEN_WIDTH / 2
final_time_rect.centery = 300

screen.blit(game_bac, (0, 0))
screen.blit(game_over_font, game_over_rect)
screen.blit(final_score, final_score_rect)
screen.blit(final_time, final_time_rect)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    key_presses = pygame.key.get_pressed()
    if key_presses[K_q]:
        exit()
    pygame.display.update()


