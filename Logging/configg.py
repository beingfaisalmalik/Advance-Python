import logging
import logging.config

#it is for getting up the logger from the config file we have already defined
logging.config.fileConfig('logs.conf')

#for setting up the name of logger

logger = logging.getLogger(__name__)

