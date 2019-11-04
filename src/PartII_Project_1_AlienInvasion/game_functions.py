# game_functions.py

# 创建了两个新函数：check_keydown_events() 和check_keyup_events() ，它们都包含形参event 和ship
# 将函数check_events 中相应的代码替换成了对这两个函数的调用。

import sys

# 13.6.2-新增-响应外星人和飞船的碰撞-使用sleep来暂停游戏
from time import sleep

import pygame

# 12.8.4开火-新增
from bullet import Bullet

# 13.3.3-新增-创建外星人群
from alien import Alien

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
    # 13.1-新增-将event加入参数列表,并在主程序响应添加event参数 - 报错，先删了event并注释13.1添加的按键Q退出程序
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
        
        # 13.1新增-结束游戏的快捷键Q
        # elif event.key == pygame.K_q:
        #     pygame.quit()
        #     sys.exit()

# 12.8.8-新增-将发射子弹的代码放在下面的独立函数中            
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
            
def update_screen(ai_settings, screen, ship, bullets, aliens):
    # 13.3.2-创建多行外星人中，将alien改为aliens
    # 13.2.3-让外星人出现在屏幕上-添加alien到参数列表
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
    # 13.2.3-新增-为让外星人出现在屏幕上，在update_screen()中调用方法blitme()
    # alien.blitme() # 先绘制子弹和飞船，再绘制外星人。在13.3.2中注释，并补充下一句
    aliens.draw(screen) # 对编组调用draw()时，pygame将自动绘制编组的每个元素，绘制位置由元素的属性rect决定
                        # 这里：aliens.draw(screen)在屏幕上绘制编组中的每个外星人
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    
# 12.8.7 新增-创建函数update_bullets()并删去主程序中响应的部分
# 13.5.3-大修-添加参数列表，并增加if判断
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    # 13.5.1-新增-检测子弹与外星人的碰撞
    # 检测是否有子弹击中了外星人，如果是，就删除相应的子弹和外星人
    # 13.5.5-重构时移到到另一个（下面那个）函数中
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        # 新增的这行代码遍历编组bullets 中的每颗子弹，再遍历编组aliens 中的每个外星人。
        # 每当有子弹和外星人的rect 重叠时，groupcollide() 就在它返回的字典中添加一个键-值对。
        # 两个实参True 告诉Pygame删除发生碰撞的子弹和外星人。
        # （要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，可将第一个布尔实参设置为False ，并让第二个布尔实参为True 。
        # 这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。）
        
    # 13.5.3-新增-生成新的外星人群
    # 13.5.5-重构时移到到另一个（下面那个）函数中
    # if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        # bullets.empty() # 为空时，用方法empty()删除编组中余下的所有精灵，从而删除现有的所有子弹
        # create_fleet(ai_settings, screen, ship, aliens)
        
    # 13.5.5-重构-上面语句移到新函数后调用
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
            
# 13.5.5-重构update_bullets()-创建了一个新函数——check_bullet_alien_collisions()
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹与外星人的碰撞"""
    # 删除发送碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # 删除现有的所有子弹，并创建一个新的外星人群
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

            
# 13.3.4-重构create_fleet()-新增函数
def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

# 13.3.5-添加行-新增函数
def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

# 13.3.4-重构create_fleet()-新增函数
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 13.3.5-新增row_number到参数列表
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 13.3.5新增
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # 13.3.5新增
    alien.rect.y = alien.rect.height = 2 * alien.rect.height * row_number
    aliens.add(alien)

# 13.3.4-重构create_fleet()-重构
# 13.3.3-新增的一个功能
def create_fleet(ai_settings, screen, ship, aliens):
    # 13.3.5新增ship到参数列表
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen) # 这个外星人不是外星人群的成员，没有将它加入到编组aliens中
    # alien_width = alien.rect.width # 从外星人的rect属性中获取宽度，并存储这个值，以免反复访问rect
    # available_space_x = ai_settings.screen_width - 2*alien_width # 计算可用于放置外星人的水平空间，以及人数
    # number_aliens_x = int(available_space_x / (2*alien_width)) # 使用int确保外星人的人数是整数。int()将小数部分丢弃
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # 13.3.5新增
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # 创建第一行外星人-13.3.5注释，放进下方包括行的for循环中
    # for alien_number in range(number_aliens_x): # 从0到要创建的外星人的数量
        # 创建一个外星人并通过设置x坐标将其加入当前行
        # alien = Alien(ai_settings, screen)
        # alien.x = alien_width + 2 * alien_width * alien_number #将每个外星人往右推一个外星人的宽度 
        # alien.rect.x = alien.x
        # aliens.add(alien) # 将每个新创建的外星人都添加到编组aliens中
        # 13.3.5注释
        # create_alien(ai_settings, screen, aliens, alien_number)
        
    # 13.3.5新增-创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

# 13.4.4-新增：编写函数check_fleet_edges() 和change_fleet_direction() ，并对update_aliens() 进行修改：
def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

# 13.4.4新增-同上
def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

# 13.6.2-新增-响应外星人和飞船的碰撞
def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    # 将ships_left减一
    # 13.6.4-新增-游戏结束响应-增加if-else语句
    if stats.ships_left > 0:
        stats.ships_left -= 1
    
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
    
        # 创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
    
        # 暂停
        sleep(0.5)
        
    else:
        stats.game_active = False
    
# 13.6.3-新增函数-有外星人达到屏幕底端
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
    
# 13.4.1-新增-向右移动外星人
# 13.6.2-新增-响应外星人和飞船的碰撞-添加ai_settings,stats,screen,ship,bullets到参数列表
def update_aliens(ai_settings, stats, ship, aliens, bullets):
    """更新外星人群众所有外星人的位置"""
    """
    13.4.4新增-检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 13.6.1-新增-检测外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens): # spritecollideany()接受两个实参：一个精灵一个编组
                                                     # 检查编组是否有成员与精灵碰撞，并在找到与精灵发送了碰撞的成员后就停止遍历编组
        # print('Ship hit!!!')
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        
    # 13.6.3-新增-有外星人达到屏幕底端-调用
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)