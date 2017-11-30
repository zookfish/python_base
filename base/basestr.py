

# encoding=UTF-8

print('包含中文的str')

# ord 获取字符的整数表示
print(ord('A'))
print(ord('中'))
# chr 编码转字符
print(chr(66))

# 字节类型
print(b'ABC')

print('ABC'.encode('utf-8'))
# 编码为字节
print('中文'.encode('utf-8'))


print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化字符串
#占位符	替换内容
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
#%% 表示一个%(相当于%%转义了一个)

print('hello %s,today is fine,we have %%%d\'s percents make $%f' % ('zookfish',90,1000000.0))
print('hello {},today is fine,we have %{}\'s percents make ${}'.format('zookfish',90,100000.1))












