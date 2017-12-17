

# python匿名函数


def m(a,b,fun):
    res = fun(a,b)
    return res

# python3会把输入的值当做字符串存贮
# python2会直接执行输入的值
func_str = input("请输入函数表达式:")

# eval 直接执行表达式
func = eval(func_str)

print(m(3,4,func))

m = [100]




