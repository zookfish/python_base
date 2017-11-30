

import os,time

# 源文件
source = ['/Users/zookfish/notes']
# 目标目录
target_dir = '/Users/zookfish/backup'


today = target_dir + os.sep + \
    time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)


zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('zip command is',zip_command)
print('Running...')

if os.system(zip_command) ==0:
    print('Successful backup to',target)
else:
    print('Backup Failed')
