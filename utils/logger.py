from loguru import logger

logger.remove()
logger.add("test_logs.log",enqueue=True, level = 'DEBUG', mode='w')