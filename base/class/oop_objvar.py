
class Robot:
    '''带有名字的机器人'''

    # 类变量  对于类变量 可以使用__开头变量命名,python会将其视为私有属性 外界无法直接访问
    __population = 0
    # 这种在类外面是直接公开的,不太安全
    test = 0

    def __init__(self,name):
        '''初始化数据'''
        self.name = name
        print('Initializing {}'.format(self.name))

        # 创建机器人数量就加1
        Robot.population +=1

    def die(self):
        '''挂了一个'''
        print('{} is being destroyed!'.format(self.name))

        Robot.population -=1
        if Robot.population ==0:
            print('{} was the last one'.format(self.name))
        else:
            print('there are still {:d} robots'.format(self.__class__.__population))

    def say_hi(self):
        '''来至机器人的问候'''
        print('hello,my master calls me {}'.format(self.name))

    # 类方法 cls表示class对象本身 @classmethod装饰器
    @classmethod
    def how_many(cls):
        print('we only have {:d} robots'.format(cls.__population))


d1 = Robot('zookfish')
d1.say_hi()
Robot.how_many()

d2 = Robot('yunux')
d2.say_hi()
Robot.how_many()


d1.die()
d2.die()

Robot.how_many()