

# python之偏函数
#         就是把某些函数的参数固定住

# eg:
import functools
# 固定住按2进制转换
int2 = functools.partial(int,base=2)

print(int2('1000000'))
