# game_functions.py

# 创建了两个新函数：check_keydown_events() 和check_keyup_events() ，它们都包含形参event 和ship
# 将函数check_events 中相应的代码替换成了对这两个函数的调用。

import sys

import pygame

# 12.8.4开火-新增
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 12.8.4-开火-将ai_settings,screen,bullets加入参数列表
    """响应按键"""
    if event.key == pygame.K_RIGHT: # 读取属性event.key，以检查按下的是否是右箭头键
        # 12.6.2新增：修改了玩家按下右箭头键时响应的方式--不直接调整飞船的位置，而是将moving_right设置为True
        ship.moving_right = True
        # 向右移动飞船
        # ship.rect.centerx += 1 # 如果按下的是右箭头键，就将ship.rect.centerx的值加1，从而将飞船向右移动
        # 12.6.3新增：左右移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    # 12.8.4-开火-新增
    elif event.key == pygame.K_SPACE:
        # 12.8.8-新增-将发射子弹的代码移到独立函数中，放到下面
        fire_bullet(ai_settings, screen, ship, bullets)
        # 创建一颗子弹，并将其加入到编组bullets中
        # 12.8.6-新增-限制子弹数量
        # if len(bullets) < ai_settings.bullets_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # 12.6.3新增
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings, screen, ship, bullets): # 1-新增：在函数check_events()中包含形参ship
    # 12.8.4-开火-新增：将ai_settings, screen, bullet加入参数列表
    # check_events()函数：存放管理事件的代码，以简化run_game()并隔离事件管理循环。
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # 别忘了这句
            sys.exit()
        elif event.type == pygame.KEYDOWN: # 添加elif代码块，以便在pygame检查到KEYDOWN事件时作出相应
            check_keydown_events(event, ai_settings, screen, ship, bullets)
                # 12.8.4-开火-新增ai_settings, screen, bullets到参数列表
        
        # 12.6.2新增：添加一个elif代码块，用于响应KEYUP事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

# 12.8.8-新增-将发射子弹的代码放在下面的独立函数中            
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
            
def update_screen(ai_settings, screen, ship, bullets):
    # 12.8.4新增-bullets到参数列表
    # update_screen()函数：存放更新屏幕的代码
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    
    # 12.8.4-开火-新增：在飞船和外星人后面重绘所有子弹
    # 为在屏幕上绘制发射的所有子弹，遍历编组bullets中的精灵，并对每个精灵都调用draw_bullet()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    
# 12.8.7 新增-创建函数update_bullets()并删去主程序中响应的部分
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)