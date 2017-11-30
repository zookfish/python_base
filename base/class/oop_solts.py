
# 使用__slots__限制类动态添加的实例属性

# 实例属性是优于类属性的
class Student(object):
    __slots__ = ('name','age','func')

def func():
    print('test')

# Student.name = 'zookfish'
# Student.age = 27
Student.sex = 'man'
# Student.func = func
s = Student()
s.func = func
s.name = 'name'
s.age = 'age'
# s.tec = 'tec'
print(s.func(),s.name,s.age,s.sex)