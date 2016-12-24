# -*- coding: utf-8 -*-
""" This is a simple way to compile Cython *.pyx code to a Python Extension Module (dynamic library)
"""
from setuptools import setup
from Cython.Build import cythonize

setup(name = 'hello', ext_modules = cythonize("hello.pyx"))
