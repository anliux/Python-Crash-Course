# 1-创建ship类
# 创建一个名为ship的模块，其中包含ship类，它负责管理飞船的大部分行为

# ship.py

import pygame

class Ship():
    
    def __init__(self, screen): # 后一个参数screen指定了要将飞船绘制到什么地方
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # 这个load函数返回一个表示飞船的surface，并存储到self.image中
        self.rect = self.image.get_rect() # 使用get_rect()获取响应surface的属性rect
                                          # 处理rect对象时，可使用矩形四角和中心的x和y坐标，通过设置这些值来指定矩形的位置
            # 居中：center，centerx，centery 与屏幕边缘对齐：top，bottom，left，right 等等
        self.screen_rect = screen.get_rect() # 首先将表示屏幕的矩形存储在self.screen_rect中
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx # 将self.rect.centerx(飞船中心的x坐标)设置为表示屏幕的矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom # 将self.rect.bottom(飞船下边缘的y坐标)设置为表示屏幕的矩形的属性bottom
        
        # 12.6.2新增：移动标志
        self.moving_right = False
        # 12.6.3新增：左右移动
        self.moving_left = False
    
    # 12.6.2新增
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1
        # 12.6.3新增：左右移动
        if self.moving_left:
            self.rect.centerx -= 1
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)