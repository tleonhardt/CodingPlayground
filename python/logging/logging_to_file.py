#!/usr/bin/env python
# coding=utf-8
"""
This is a simple example of using Python's logging module to log to a file.

Expected output (to file 'example.log' in same directory as script is run):
    DEBUG:root:This message should go to the log file
    INFO:root:So should this
    WARNING:root:And this, too

This example also shows how you can set the logging level which acts as the threshold for tracking.
In this case, because we set the threshold to DEBUG, all of the messages were printed.
"""
import logging

LOG_FILE = 'example.log'

LOG_LEVEL = logging.DEBUG

APPEND = False
if APPEND:
    mode = 'a'
else:
    mode = 'w'

# Note the "8s" right-justifies the levelname in an 8-char wide field.  For left justification, use "-8s" instead.
LOG_FORMAT = '%(asctime)s - %(levelname)8s: %(message)s'

logging.basicConfig(filename=LOG_FILE, filemode=mode, format=LOG_FORMAT, level=LOG_LEVEL)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('{} before you {}'.format('Look', 'leap!'))
