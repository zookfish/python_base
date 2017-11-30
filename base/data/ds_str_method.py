

name = 'zookfish'

if name.startswith('zoo'):
    print('字符串是以zoo开头')

if 'f' in name:
    print('字符f是包含在name中')

if name.find('war') !=-1:
    print('name中不包含有war')

delimiter = '_*_'
mylist = ['zoo','runn','india','china']
print(delimiter.join(mylist))
