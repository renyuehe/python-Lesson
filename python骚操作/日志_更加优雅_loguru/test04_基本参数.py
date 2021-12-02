from loguru import logger

logger.add('runtime.log', format="{time} {level} {message}", filter="my_module", level="INFO")

