
# 元类
# 动态创建一个类

def fn(self,name='zookfish'):
    print('hello %s' % name)
# 动态的创建一个类
'''
    type函数后面对应的参数
    1:要创建的类名
    2:tuple 继承的类  支持多继承
    3:绑定的方法 方法名称和方法
'''
Test = type('Hello',(object,),dict(hello=fn))

h = Test()
h.hello()

