# settings.py
# 用于将所有设置存储在一个地方，让代码调用更简单，且在项目增大时修改游戏的外观更容易

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 12.6.4新增-调整飞船的速度
        self.ship_speed_factor = 1.5 # 改为每次移动1.5像素
                                     # 然而rect的centerx等属性只能存储整数值，因此对Ship类做些修改
        
        # 13.6.2-新增-响应外星人和飞船碰撞
        self.ship_limit = 3
        
        # 12.8.1新增-子弹设置
        # 创建宽3像素，高15像素的深灰色子弹，子弹的速度比飞船稍低
        # 13.5.4-提高子弹速度-修改子弹速度从1改为3
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 12.8.6新增-限制子弹数量-将未消失的子弹数限制为3
        self.bullets_allowed = 3
        
        # 13.4.1-新增-向右移动外星人-添加一个控制外星人速度的设置：
        self.alien_speed_factor = 1
        
        # 13.4.2-新增-创建表示外星人移动方向的设置
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
            # fleet_direction为1表示向右移，为-1表示向左移