# alien.py

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        # 将每个外星人的左边距设置为外星人的宽度，上边距设置为外星人的高度
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        
    # 13.4.2-新增-检查外星人是否撞到了屏幕边缘
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    # 13.4.1-新增-向右移动外星人-在settings.py里设置外星人速度，并在alien.py中用update()来实现
    def update(self):
        """向右或左移动外星人"""
        # 13.4.2-修改-为左右移动外星人，并修改下面的公式
        # self.x += self.ai_settings.alien_speed_factor # 使用属性self.x根据每个外星人的准确位置，这个属性可存储小数值
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction) # 乘以方向，而方向是正负1，非常巧妙
        self.rect.x = self.x # 使用self.x的值来更新外星人的rect的位置
         
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)