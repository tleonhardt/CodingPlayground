Building
========

Building Using distutils
-------------------------
python setup.py build_ext
python setup.py install --install-platlib=.


Building Manually
-----------------
Create the SWIG interface file to wrap the library
    - Located in "example.i"


Auto-generate wrapper code with SWIG
- Use SWIG to generate the "example_wrap.c" C file and "example.py" Python extenstion module wrapper code
    swig -Wall -python example.i


Building a Python module:
1) Use gcc to compile the Python extension module as a shared library "_example.so" which is importable in Python and links to Python
    gcc -fPIC -Wall -Wextra -c example.c example_wrap.c -I/home/todd/anaconda3/include/python3.5m
    ld -shared example.o example_wrap.o -o _example.so


Using the Python Module
=======================

Running with test.py
--------------------
python test.py
