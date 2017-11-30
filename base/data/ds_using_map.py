

# python高阶函数  都可以接收函数为参数
# map(f,Iterable) 返回一个迭代器对象
from collections import Iterator,Iterable
from functools import reduce
def f(s):
    return s * s

it = map(f,[1,2,3,4,5])
print(it)
print(isinstance(it,Iterable))
print(isinstance(it,Iterator))


print(list(it))
print([x * x for x in [1,2,3,4,5]])


# reduce(f,list)  redus把函数应用于列表的每两个元素 只能对应两个参数

def mul(x,y):
    return x + y

def multest(x,y,z):
    return x + y +z

s = reduce(mul,(1,2,3,4,5))
print(s)
# st = reduce(multest,(1,2,3,4,5))
# print(st)



# filter  过滤序列
def fi(i):
    return i % 2 ==1
f = filter(fi,(1,2,3,4,5,6))
print(f)
print(next(f))
print(list(f))


# sorted
print(sorted(['a','B','C','d','G'],key=str.lower,reverse=True))





