
# encoding=UTF-8

import sys,time
f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) ==0:
            break
        print(line,end='')
        sys.stdout.flush()
        time.sleep(2)

except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('Cancelled')

finally:
    if f:
        f.close()
    print('Cleaning up')
