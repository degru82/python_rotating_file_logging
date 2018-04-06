#!/usr/local/bin/python3

import logging
import logging.handlers
from logging.config import fileConfig

import log_son

# If you want to stream out all the logs to the screen,
# the following block will be enough

# myformat = '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
# myhandler = logging.handlers.RotatingFileHandler(filename='mytest.log', mode='w', maxBytes=10000, backupCount=5)
# logger = logging.getLogger("root") 
# logging.basicConfig(level=logging.DEBUG, handlers=[myhandler], format=myformat)

# If you want to record all the logs into a file,
# you need to do it with the following 2 lines here
# disable_existing_loggers should be set to False in order to record sub-module's logging
fileConfig('log_config.ini', disable_existing_loggers=False)
logger = logging.getLogger("root") 



# log testing

logger.debug('MOM-DEBUG')
logger.info('MOM-INFO')

log_son.do_logging()

logger.warning('MOM-WARNING')
logger.error('MOM-ERROR')