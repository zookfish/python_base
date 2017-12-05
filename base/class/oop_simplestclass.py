
class Person:

    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    # 类方法
    def say_hi(self):
        print('Hello,my name is',self.__name)
# Pserson类实例化会调用__init__方法
p = Person('zookfish')
p.say_hi()
# 实例属性 公共的  只要 在属性前面加上__ 就会变温私有的
print(p.__class__)
print(p.getName())