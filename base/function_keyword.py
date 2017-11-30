

# 关键字参数
def func(a,b=5,c=10):
    print('a is:',a,'and b is:',b,'and c is:',c)

# 关键字参数可以指定参数名来给参数赋值
func(5)
func(6,7,8)
func(a=5)
func(a=10,b=11,c=12)
func(a=1,c=19)
func(a=12,b=13)
# func(a=9,d=100) 报错不存在指定参数名
# func(99,100,101,102) 参数个数也是不满足的
