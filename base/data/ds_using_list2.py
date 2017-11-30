

import os
# 列表生成式   [x for x in 'abc'] 生成式通过[]包裹
print([m + n for m in 'abc' for n in 'dce'])

# print([d for d in os.listdir('/Users/zookfish')])

# 生成器   生成器通过()包裹
# 打印一个对象 <generator object <genexpr> at 0x1032cb4c0> 表示是一个生成器对象
g = (x for x in 'abc')
print(g)
# 得到生成器的每个值
#print(next(g))
#print(next(g))
#print(next(g))
# 当genrater遍历完了就会报错
# print(next(g))
# so 通过for来遍历
for v in g:
    print(v)

# 斐波拉切数列
# 1 1 2 3 5 8
def fib(n):
    fibs =  []
    tmp,a,b = 0,0,1
    while tmp < n:
        fibs.append(b)
        a,b = b,a+b
        tmp +=1
    return fibs

print(fib(6))

a = 3
b = 4
# a,b = b,a+b  写在一句里面确实有点容易理解错误

#a=b
#b=a+b
a,b = b,a  #交换a,b的值
print(a,b)







