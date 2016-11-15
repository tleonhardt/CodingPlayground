# -*- coding: utf-8 -*-
""" This example displays how to use pyximport for on-the-fly compilation via Cython.

For simple cases like this example, pyximport removes the need to write a setup.py
distutils script, and we can treat hello.pyx as if it were a regular Python module.

If a Cython source file is modified, pyximport automatically detects the modification
and will recompile the source file the next time it is imported in a new Python
interpreter session.

Because Cython modules imported via pyximport depend on both the cython compiler and a
properly set up C compiler, it tends not to be used in production environments where
these dependencies are not under our control.
"""
import pyximport

# .install() needs to be called before importing Cython extension modules
pyximport.install()

# This will compile hello.pyx to a *.so if it hasn't already been and load the .so extension module
import hello

hello.say_hello_to('Todd')

