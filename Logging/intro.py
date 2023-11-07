import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.exception('exp')