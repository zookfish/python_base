

shopList = ['apple','mango','banana','carrot']
shopList2 = ['apple','mango','banana','carrot']
# 将shopList指向的对象地址赋值给shopList
myList = shopList

del shopList[0]
print(myList)
print(shopList)

# 这里是生成一个副本赋值给mylist
myList = shopList2[:]
del shopList2[0]
print(myList)
print(shopList2)
