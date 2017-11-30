
# 这句引用对下面带属性的装饰器很重要
from functools import wraps

# python 装饰器 一个能返回函数的高阶函数
def now():
    print('2015-3-25')

f = now
# 这里打印函数的返回值,默认为none
print(f())

# 获取函数名
print(f.__name__)
print(now.__name__)

# 定义一个装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
# 定义带属性的装饰器
def log(text):
    def decorator(func):
        # 相当于wrapper.__name__ = func.__name__
        @wraps(func)
        def wrapper(*args,**kw):
            print('%s %s' % (text,func.__name__))
            func(*args,**kw)
        return wrapper
    return decorator



@log('hello')
def today():
    print('pengyufang baby，I love you!')

today()
# 解决装饰器 返回函数时，函数名不一致的问题
print(today.__name__)






