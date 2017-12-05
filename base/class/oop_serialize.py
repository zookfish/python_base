

# python 的序列化
# pickle模块

import pickle
import json
d = dict(name='zookfish',age=26,email='test@sina.com')
# 对象序列化到文件
with open('pickle.dump','wb') as f:
    pickle.dump(d,f)

# 反序列化
with open('pickle.dump','rb') as f:
    ds = pickle.load(f)
    print(ds)


# python的序列化只能支持python语言
# json格式的序列化
with open('json.dump','w') as f:
    json.dump(d,f)

with open('json.dump','r') as f:
    dj = json.load(f)
    print(dj)
