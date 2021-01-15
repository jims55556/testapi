# -*- coding:utf-8 -*-
import logging

logger=logging.getLogger()
fh=logging.FileHandler('test.log')
formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')





# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='testlog.log',
#                     filemode='a')
#
#
# logging.debug('debug2')
# logging.info('info2')
# logging.warning('warning2')
# logging.error('error2')
# logging.critical('critical2')
