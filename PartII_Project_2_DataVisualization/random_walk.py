# random_walk.py
from random import choice # 每次做决策时都是用choice()来决定使用哪种选择

class RandomWalk():
    """一个生产随机漫步数据的类"""
    
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        
        # 所有随机漫步都始于（0,0）
        # 创建两个用于存储x和y值的列表，并让每次漫步都从(0,0)出发
        self.x_values = [0]
        self.y_values = [0]
        
    # 15.3.2新增：def fill_walk()
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        # 不断漫步，直到列表达到指定的长度
        # 这个方法的主要部分告诉Python如何模拟四种漫步决定：向右走还是向左走？沿指定的方向走多远？
        # 向上走还是向下走？沿选定的方向走多远？
        while len(self.x_values) < self.num_points:
            
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1]) # 方向：要么向右1，要么向左-1
            x_distance = choice([0, 1, 2, 3, 4]) # 距离：0-4选择沿指定方向走多远
                                                 # 距离0：沿某轴移动
            x_step = x_direction * x_distance  # 确定沿x轴移动的距离
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance  # 确定沿y轴移动的距离
            
            # 拒绝原地踏步：两个step都是0意味着原地踏步，这时continue继续循环
            if x_step == 0 and y_step == 0:
                continue
            
            # 计算下一个点的x和y值
            # 将step与values中的最后一个数即[-1]相加，得到下一个点的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            # 将下一个点的值附加到x和y值列表的后面
            self.x_values.append(next_x)
            self.y_values.append(next_y)