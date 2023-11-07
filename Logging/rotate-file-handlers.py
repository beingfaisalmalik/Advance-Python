#used to create a backup for the logs

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
handler = RotatingFileHandler('app.log', maxBytes=2000,backupCount=5)

logger.addHandler(handler)
for i in range(1000):
    logger.error('This is error')