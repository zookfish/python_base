

# 可迭代对象  Iterable

# import collections
from collections import Iterable,Iterator

# 可迭代对象 只能被用于for循环  Iterable
# 字典
print(isinstance({},Iterable))
# 列表
print(isinstance([],Iterable))
# 字符串
print(isinstance('',Iterable))
# set
print(isinstance((['a','b']),Iterable))
# tuple
print(isinstance(('a',),Iterable))

# 迭代器对象  Iterator Iterator对象可以被next()不断调用,没有元素就跑出StopIteration 异常,懒加载
print(isinstance({},Iterator))
print(isinstance([],Iterator))
print(isinstance('',Iterator))
print(isinstance((['a','v']),Iterator))
print(isinstance(('a',),Iterator))