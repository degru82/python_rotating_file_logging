#!/usr/local/bin/python3

import logging

logger = logging.getLogger('GRANDSON')

def do_logging():
    logger.debug('GRANDSON-DEBUG')
    logger.info('GRANDSON-INFO')
    logger.warning('GRANDSON-WARNING')
    logger.error('GRANDSON-ERROR')
