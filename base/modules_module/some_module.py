

import sys
import os
import platform
import logging


print(platform.platform())
logging_file = os.path.join(os.getenv('HOME'),'test.log')

logging.basicConfig(
    level=logging.DEBUG,
    format=('%(asctime)s : %(levelname)s : %(message)s'),
    filename=logging_file,
    filemode='a',
)

logging.debug('Start od the program')
logging.info('Doing something')
logging.warning('Dying now')



print(os.environ)
print(os.getenv('HOME'))
print(sys.version_info)


