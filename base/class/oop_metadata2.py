
# 使用metaclass 创建对象


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

        type.__new__()


# 自定义类 指定元类 创建Mylist对象会通过ListMetaclass.__new__来创建
class Mylist(list,metaclass=ListMetaclass):

    pass


l = Mylist()
l.add('mm')
print(l)

