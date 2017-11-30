
class Person:

    def __init__(self,name):
        self.name = name


    # 类方法
    def say_hi(self):
        print('Hello,my name is',self.name)
# Pserson类实例化会调用__init__方法
p = Person('zookfish')
p.say_hi()