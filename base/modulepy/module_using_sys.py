
# import 引入sys模块  避免使用from 防止两个模块里面有相同的变量
import sys,os
from math import sqrt


print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')
print(os.getcwd())

print("Square root of 16 is",sqrt(16))
print(sqrt(16) ==4)
__version__ = '0.2'