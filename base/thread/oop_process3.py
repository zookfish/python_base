
# 进程间的通信  通过Queue传递进行进程间的通信
from multiprocessing import Process,Queue
import os,time,random

# 写数据进程执行的代码
def write(q):
    print('开始写数据:%s' % os.getpid())
    for v in ['a','b','c','d']:
        print('放进队列值为:%s' % v)
        q.put(v)
        time.sleep(random.random())

# 读数据
def read(q):
    print('开始读数据:%s' % os.getpid())
    while True:
        v = q.get(True)
        print('获得值为:%s' % v)

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pw.join()

    # 强制结束进程
    pr.terminate()
