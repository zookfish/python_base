

shopList = ['apple','mango','carrot','banana']
test = ["2","1","3"]

print("I have",len(shopList),'items to purchase')

print('These items are',end=' ')
for item in shopList:
    print(item,end=',')

print('\nI have also to buy rice')
shopList.append('rice')
print('MyShopping list is now',shopList)

# 注意extend和append的区别
# shopList.extend(test)  看我extend ['apple', 'mango', 'carrot', 'banana', 'rice', '2', '1', '3']
# print("看我extend",shopList)
# shopList.append(test)
# print("看我append",shopList) 看我append ['apple', 'mango', 'carrot', 'banana', 'rice', '2', '1', '3', ['2', '1', '3']]



# sort要被调用必须要类型相同
shopList.sort()
print('Sorted shopping list is', shopList)

print('The first item I will buy is',shopList[0])

oldItem = shopList[0]
del shopList[0]
print('I bought the ',oldItem)
print('MyShopping list is now',shopList)

# 列表生成式
print([s * s for s in range(1,6) if s % 2 ==0])
