from setuptools import setup
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

setup(
    name = "cyfib",
    ext_modules = cythonize('cyfib.pyx', compiler_directives={'embedsignature': True}),
)
