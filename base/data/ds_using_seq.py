
shopList = ['apple','mango','carrot','banana']
name = 'yunux'

print('Item 0 is',shopList[0])
print('Item 1 is',shopList[1])
print('Item 2 is',shopList[2])
print('Item 3 is',shopList[3])
print('Item -1 is',shopList[-1])
print('Item -2 is',shopList[-2])

print('Character 0 is',name[0])

# 切割list  前闭后开
print('Item 1 to 3 is',shopList[1:3])
print('Item 2 to end is',shopList[2:])
print('Item 1 to -1 is',shopList[1:-1])
print('Item start to end is',shopList[:])
print('加上步长之后',shopList[:3:2])

# 从某个字符串开始切割
print('character 1 to 3 is',name[1:3])
print('character 2 to end is',name[2:])
print('character 1 to -1 is',name[1:-1])
print('character start to end is',name[:])