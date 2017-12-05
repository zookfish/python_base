

# python的进程
from multiprocessing import Process
import os
# print('Process (%s) start...' % os.getpid())
# 父进程执行一遍,子进程执行一遍
# pid = os.fork()
# if pid ==0:
#     print('子进程 (%s) and 父进程 (%s)' % (os.getpid(),os.getppid()))
# else:
#     print('我(%s) 创建了一个子进程 (%s)' % (os.getpid(),pid))


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start')
    # 创建
    p.start()

    p.join()
    print('Child process end.')