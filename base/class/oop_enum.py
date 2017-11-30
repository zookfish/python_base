
# enum 枚举类

from enum import Enum
DATAS = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
print(DATAS(1))
for k,v in DATAS.__members__.items():
    print(k,'',v)