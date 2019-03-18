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