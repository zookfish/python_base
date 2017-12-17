

class T(object):

    def __init__(self):
        print("初始化")

    def __del__(self):
        print("销毁对象")

    def __str__(self):
        print("打印对象的时候会调用")
        return ""

    def __new__(cls, *args, **kwargs):
        print("创建对象")
        # 注意这里需要返回创建的对象
        return object.__new__(cls)


t = T()
print(t)
del t