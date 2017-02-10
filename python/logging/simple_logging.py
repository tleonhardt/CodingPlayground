#!/usr/bin/env python
# coding=utf-8
"""
This is an exteremely simple example of using Python's logging module in the most basic way.

Expected output (to console stdout):
    WARNING:root:Watch out!

The INFO message doesn’t appear because the default level is WARNING.
"""
import logging

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
