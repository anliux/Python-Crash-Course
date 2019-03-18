# 1-响应按键
# 每当用户按键时，都在pygame中注册一个事件，事件通过方法pygame.event.get()获取的
# 因此在函数check_events()中，需要指定要检查哪些类型的事件
# 每次按键都被注册为一个KEYDOWN事件

# game_functions.py
# 导入事件循环要使用的sys和pygame
import sys

import pygame

def check_events(ship): # 1-新增：在函数check_events()中包含形参ship
    # check_events()函数：存放管理事件的代码，以简化run_game()并隔离事件管理循环。
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # 别忘了这句
            sys.exit()
        
        # 1-响应按键
        elif event.type == pygame.KEYDOWN: # 添加elif代码块，以便在pygame检查到KEYDOWN事件时作出相应
            if event.key == pygame.K_RIGHT: # 读取属性event.key，以检查按下的是否是右箭头键
                # 12.6.2新增：修改了玩家按下右箭头键时响应的方式--不直接调整飞船的位置，而是将moving_right设置为True
                ship.moving_right = True
                # 向右移动飞船
                # ship.rect.centerx += 1 # 如果按下的是右箭头键，就将ship.rect.centerx的值加1，从而将飞船向右移动
            # 12.6.3新增：左右移动
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        # 12.6.2新增：添加一个elif代码块，用于响应KEYUP事件
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            # 12.6.3新增
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            
def update_screen(ai_settings, screen, ship):
    # update_screen()函数：存放更新屏幕的代码
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()