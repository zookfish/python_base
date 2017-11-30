

# 函数可以返回函数

def cal_sum(*args):
    def sum():
        total = 0
        for i in args:
            total += i
        return total

    return sum

li = [1,2,3,4,5,6]
f = cal_sum(*li)
print(f)
print(f())



def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())