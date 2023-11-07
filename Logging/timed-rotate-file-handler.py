import logging
from logging.handlers import TimedRotatingFileHandler
import time
logger = logging.getLogger(__name__)

handler = TimedRotatingFileHandler('app.log',when='s',interval=5,backupCount=5)
logger.addHandler(handler)

for i in range(1000):
    logger.error('This is the error')
    time.sleep(5)