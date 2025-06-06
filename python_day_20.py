class Car:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0##里程数
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,num):
        """打印一条指出汽车行驶里程的消息"""

        if num < self.odometer_reading:
            print("You can't roll back an odometer!")
            self.odometer_reading = self.odometer_reading
        else:
            self.odometer_reading = num


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
####完啦，我把我要写的代码给删除了
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        # 调用父类构造函数   super()._这个函数是继承当中调用父类函数的方法

        self.battery = Battery(50)
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery.battery_size == 40:
            range = 150
        elif self.battery.battery_size == 65:
            range = 225
        else:
            range = "未知"


        print(f"This car can go about {range} miles on a full charge.")


    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.(重写版本)")####子类的代码覆盖父类的相同代码，更新





my_new_car = ElectricCar('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1)###更新的功能1
my_new_car.read_odometer()

##类的继承

# my_new_car.describe_battery()

##类的模块使用
my_new_car.battery.describe_battery()