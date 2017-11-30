

# 生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        # 函数会返回b这个值
        yield b
        a,b = b,a+b
        n +=1

    return 'done'
# 如果一个函数含有yield关键字,则这个函数就是一个生成器
f = fib(6)
print(f)
# for循环拿不到generate的返回值
# for v in f:
#     print(v)




while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.value)
        break

