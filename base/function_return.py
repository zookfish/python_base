
def maximum(x,y):
    '''
    :param x:
    :param y:
    :return:
    : 比较两个数字中的较大数
    '''
    x = int(x)
    y = int(y)
    if x > y:
        return x
    elif x == y:
        return '两个数字相等'
    else:
        return y

def some_func():
    pass

# 每个函数都隐式的包含return None None是python的一种数据类型
print(some_func())

print(maximum(4,4))
print(maximum(3,4))
# 打印函数的doc说明文档
print(maximum.__doc__)


