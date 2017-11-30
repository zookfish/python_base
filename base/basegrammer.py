

# #作为python语言的注释

# 单引号 双引号 三引号
# 三引号 可以包含多行字符串
print('hello,maohao')
print("hello,zookfish")

print('''
	This is the second line.
	"What's your name?," I asked.
	He said "Bond, James Bond."
	''')

# format 的用法   str.format()
print('{} is a great and beautiful {}'.format('pengyufang','wife'))
# 对于浮点数保留三位小数
print('{0:.3f}'.format(1.0/3))
print('{0:_^12}'.format('hello'))
print("{who}'s name is {what}".format(who = 'he',what = 'zookfish'))

print('a',end='')
print('b',end='\n')
print('c')

# \ 转义符号
print('what\'s your name?')

# python的数据类型
# 字面量 数字(int float) 字符串




