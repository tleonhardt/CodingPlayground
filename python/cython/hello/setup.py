# -*- coding: utf-8 -*-
""" This is a simple way to compile Cython *.pyx code to a Python Extension Module (dynamic library)
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(name = 'Hello world app', ext_modules = cythonize("hello.pyx"))
