import logging
import time

botLogger = None
FORMAT = '%(levelname)s at %(asctime)s: %(message)s'
FILENAME = 'logs/log'+time.ctime(None)+'.log'
FILEMODE = 'w'


class OverwriteForbiddenError(Exception):

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'Trying to change logging config arguement: {}'.format(self.arg)


def init(**kwargs):
    global botLogger
    if 'format' in kwargs:
        raise OverwriteForbiddenError('format')
    if 'filename' in kwargs:
        raise OverwriteForbiddenError('filename')
    if 'filemode' in kwargs:
        raise OverwriteForbiddenError('filemode')

    logging.basicConfig(format=FORMAT, filename=FILENAME, filemode=FILEMODE, **kwargs)
    botLogger = logging.getLogger()


# debug is just info about sth's current state
def debug(msg):
    botLogger.debug(msg)


# info is everything sth does
def info(msg):
    botLogger.info(msg)


# warning is sth that may lead to an error, but is not necessarily wrong (enexpected state, ...)
def warning(msg):
    botLogger.warning(msg)


# error is everything that prevents a function complete what it's trying to do,
# but does not affect the program by itself
def error(msg):
    botLogger.error(msg)


# critical is stuff that affects the program itself and prevents it from functioning
def critical(msg):
    botLogger.critical(msg)
