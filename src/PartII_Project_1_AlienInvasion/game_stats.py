# game_stats.py

class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats() # 在方法reset_stats()中初始化大部分统计信息，而不是在__init__()中直接初始化他们
        
        # 13.6.4-新增-结束游戏
        self.game_active = True
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit # ships_left -其值在游戏运行期间将不断变化。
                                             #一开始玩家拥有的飞船数存储在settings.py的ship_limit 中：