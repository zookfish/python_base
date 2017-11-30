

import mymodule

# mymodule.say_hi()
# print('Version',mymodule.__version__)
a = 10
# 列出指定模块的属性
print(dir(mymodule))
# 列出当前模块的属性
print(dir())
del a
print(dir())

