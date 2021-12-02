''''''
'''
loguru 还可以配置文件的压缩格式，比如使用 zip 文件格式保存，示例如下：
logger.add('runtime.log', compression='zip')
'''

from loguru import logger

logger.add('runtime.log', compression='zip')

logger.add('runtime.log')
logger.debug('this is a debug')