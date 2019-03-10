# 第9章 9.4.1 导入单个类

class Car():   
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
 
 # 在editplus里编辑空格之类的，import竟然失败，说是空格不对，复制到jupyter里一看空格果然不对劲。。不知道为啥



 # 9.4.2 - 在一个模块中存储多个类：加入类Battery和ElectricCar
 class Battery():
    """一个模拟电动汽车的简单尝试"""
    
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + '-kWh battery.')
    
    # 给电池类新加一个功能，而不会搞乱各种东西
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性        
        """
        super().__init__(make,model,year)
        self.battery = Battery()
