from loguru import logger
import sys

logger.remove(0)
logger.add(sys.stdout, level="INFO")
