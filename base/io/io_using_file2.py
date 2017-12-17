

# 读写文件

p = '''
    在我心中
    曾经有一个梦
    要让所有代码都在我的脑中
'''
f = open("test.txt","a+")
print(f.name)
f.write(p)

# while True:
#     line = f.readline()
#     print(line)
#     if line==0:
#         break

f.close()