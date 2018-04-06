#!/usr/local/bin/python3

import logging
import log_grandson

logger = logging.getLogger('SON')

def do_logging():
    logger.debug('SON-DEBUG')
    logger.info('SON-INFO')
    log_grandson.do_logging()
    logger.warning('SON-WARNING')
    logger.error('SON-ERROR')