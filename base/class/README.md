
### python的面向对象
#### python的私有属性
+ 在python中属性前面加上__双下划线就是表明这是一个私有属性,外界无法直接访问
```python
class Message:
    # 这是一个私有的方法
    def __send_msg(self):
        print("发送")
    
    # 暴露一个对外的方法,方法的实际操作不暴露给外面   
    def send_msg(self,money):
        if money <=0:
            print("输入的参数有误")
        else:
            self.__send_msg()
```
+ __de_方法 删除对象的所有引用就会调用
```python
class T:
    
    def __del__(self):
        print("所有引用已经被删除")
        

t = T()
tt = t
del t
del tt
# 只有删除上面两个对象,才会调用__del__方法
```
+ 继承
+ 多态

+ 类属性,实例属性 类方法,实例方法,静态方法
 + 类方法
  ```python
    
class T:
    # 类属性
    num = 0
    
    # 类方法
    @classmethod
    def test(cls):
        cls.num = 100
    # 静态方法
    @staticmethod
    def test2():
        print("静态方法")
        
    # 实例方法
    def test3(self):
        print("我是实例方法")
        
    # 这些方法的差别已经简单明了了
  ```
  
+ __new__ 特殊方法创建对象

 ```python
class T:
    def __new__(cls, *args, **kwargs):
        print("创建对象")
        return object.__ne__(cls)
        
    def __init__(self):
        print("init初始化 T init")
# 这里会先调用__new__ 创建对象,调用__init__初始化对象里面的属性  
t= T()
    

 ```  
  
