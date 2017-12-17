# 字符串的常用操作

mystr = 'hello zookfish echo'
print(mystr.find('e'))
# 从左边找
print(mystr.find('pyf'))
# 从右边查找
print(mystr.rfind('e'))

print(mystr.index('zook'))
# 找不到会报错
# print(mystr.index('pyf'))


print(mystr.count('zook',0,len(mystr)))
mystr_rep=mystr.replace('zookfish','pyf')

print(mystr)
print(mystr_rep)

# 恶心的for else
nums = [1,2,3,4,5]
for n in nums:
    if 5==n:
        print("有这个东东")
        # 如果break了下面的else是不会执行的
        break
else:
    print("并没有")














