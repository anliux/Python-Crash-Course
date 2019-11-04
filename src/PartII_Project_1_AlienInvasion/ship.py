# ship.py

import pygame

class Ship():
    
    def __init__(self, ai_settings, screen): # 后一个参数screen指定了要将飞船绘制到什么地方
            # 12.6.4新增-添加ai_settings，让飞船能够获取其速度设置
            
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        
        # 12.6.4新增-将形参ai_settings的值存储在一个属性中，以便能够在update()中使用它
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # 这个load函数返回一个表示飞船的surface，并存储到self.image中
        self.rect = self.image.get_rect() # 使用get_rect()获取响应surface的属性rect
                                          # 处理rect对象时，可使用矩形四角和中心的x和y坐标，通过设置这些值来指定矩形的位置
            # 居中：center，centerx，centery 与屏幕边缘对齐：top，bottom，left，right 等等
        self.screen_rect = screen.get_rect() # 首先将表示屏幕的矩形存储在self.screen_rect中
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx # 将self.rect.centerx(飞船中心的x坐标)设置为表示屏幕的矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom # 将self.rect.bottom(飞船下边缘的y坐标)设置为表示屏幕的矩形的属性bottom
        
        # 12.6.4新增-在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        
        # 12.6.2新增：移动标志
        self.moving_right = False
        # 12.6.3新增：左右移动
        self.moving_left = False
    
    # 12.6.2新增
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 12.6.5 修改：更新飞船的center值，而不是rect
        # 12.6.5-在修改self.center前检查飞船的位置。self.rect.right返回飞船外接矩形的右边缘的x坐标
        #       如果这个值小于self.screen_rect.right的值，就说明飞船未触及屏幕右边缘
        # if self.moving_right:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            # 12.6.4修改上一句为：
            self.center += self.ai_settings.ship_speed_factor
        
        # 12.6.3新增：左右移动
        # 12.6.5新增：左边缘类似：如果rect的左边缘x坐标大于0，就说明飞船未触及屏幕左边缘
        # if self.moving_left:
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            # 同上，12.6.4修改为
            self.center -= self.ai_settings.ship_speed_factor
            
        # 12.6.4新增：根据self.center更新rect对象
        # 更新self.center后，再根据它来更新控制飞船位置的self.rect.centerx，self.rect.centerx将只存储self.center的整数部分
        self.rect.centerx = self.center
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    # 13.6.2-响应外星人和飞船碰撞-新增函数
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx