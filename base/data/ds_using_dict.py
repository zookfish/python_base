

from collections import Iterable

ab = {
    'Swaroop':'swaroop@baidu.com',
    'larry':'latty@qq.com',
    'Jack':'jack@taobao.com',
    'lucy':'lucy@google.com',
    (1,2,3):'woshi tuple'
}
print('lucy\'s mail is',ab['lucy'])
for name,mail in ab.items():
    print('Contact {} at {}'.format(name,mail))

ab['yunux'] = 'yunux@wdai.com'
if 'yunux' in ab:
    print('\nyunux\'s address is',ab['yunux'])



# print(ab['test'])
# 避免因为key不存在报错
print(ab.get('test',-1))
print('test' in ab)
# set 只能接收一个list
print(set([2,3,4,5]))


# 遍历字典  keys values items
for i in ab:
    print(i,ab[i])

for v in ab.values():
    print(v)


for k,v in ab.items():
    print(k,v)


print("#####################")
# 判断是否是可迭代对象

print(isinstance('abc',Iterable))
print(isinstance(['a','b','c'],Iterable))
print(isinstance(123,Iterable))


for i,value in enumerate(['1','b','c']):
    print(i,value)



