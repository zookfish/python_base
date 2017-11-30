
# 全局变量
x = 50
# def func(x):
#     print('x is ',x)
#     # 局部变量
#     x = 2
#     print('Changed local x to',x)


def func():
    global x
    print('x is ',x)
    x = 3
    print('changed x to',x)


func()
print('x id still',x)

global m
# 注释掉此句报错,说明python在使用变量之前必须要初始化
m = 4
print(m)




