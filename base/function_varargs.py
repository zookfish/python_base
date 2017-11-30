
# 可变参数
# *nums 所有位置参数都会被汇集成为一个元组
# **phonebook 所有的关键字参数被汇集成为一个字典
def total(a=5,*nums,**phonebook):
    print('a',a)

    for single_item in nums:
        print('single_item',single_item)

    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

# 10 先被赋值给a
# 1,2,3(看做位置参数) 赋值给了nums元组
# Jack=1123,Jhon=2231,Inge=1569(看做是关键字参数) 赋值给了phonebook字典
print(total(10,1,2,3,Jack=1123,Jhon=2231,Inge=1569))