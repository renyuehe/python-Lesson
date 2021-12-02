''''''
'''
loguru 在输出 log 的时候还提供了非常友好的字符串格式化功能，像这样：

logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
'''

from loguru import logger
logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')