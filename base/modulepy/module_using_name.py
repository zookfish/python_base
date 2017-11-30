

# 每个模块都有__name__属性 如果值为__main__ 则代表这个模块是由用户独立运行
if __name__ == '__main__':
    print('running for itself')
else:
    print('being import by another module')