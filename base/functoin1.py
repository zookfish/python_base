

def say_hello():
    print('hello,zookfish')

say_hello()

# 显然python 在使用变量或者方法之前必须要先定义

def print_max(a,b):
    if (a > b):
        print(a, 'is maximum')
    elif a==b:
        print(a,'is equal to',b)
    else:
        print(b,'is maximum')

print_max(3,4)
