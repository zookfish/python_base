

# 使用@property来简化代码

class Students(object):
    # 读属性
    # @property
    # def score(self):
    #     return self._score
    #
    # # 写属性
    # @score.setter
    # def setScore(self,v):
    #     if not isinstance(int,v):
    #         raise ValueError('类型不正确')
    #     if v < 0 or v >100:
    #         raise ValueError('参数不合法')
    #     self._score = v
    # _birth = 0

    # def __init__(self):
    #     self._birth = 0
    def __init__(self,sex):
        self.sex = sex

    @property
    def birth(self):
        print('getter方法被调用')
        return self._birth

    @birth.setter
    def birth(self, value):
        print('setter方法被调用')
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


    def __getattr__(self, item):
        return None

# print(Students._birth)
# 这是一个类属性
Students._birth = 1000
print(dir(Students))
s = Students('test')
print(dir(s))
Students.sex = 'man'
# setter方法被调用
# s.birth = 1991
print(s.birth)
print(s.sex)
# print(s.)
# print(type(s.birth))
# print(type(s.age))
# s.birth(1991)
# print(s.age)


print(s.gggg)


