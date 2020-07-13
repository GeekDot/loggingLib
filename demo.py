#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from loggingLib import log

logger = log.get(__file__)


def main_1():
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')


def main_2():
    logger.error('error')
    logger.critical('critical')


main_1()
main_2()


from loggingLib import LoggingLib

log = LoggingLib('./logs')
logging = log.get(__file__)


def main_3():
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')


def main_4():
    logging.error('error')
    logging.critical('critical')


main_3()
main_4()
