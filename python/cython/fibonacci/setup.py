from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    ext_modules=[Extension('fib', ['fib.pyx'])],
    cmdclass={'build_ext': build_ext} 
)
