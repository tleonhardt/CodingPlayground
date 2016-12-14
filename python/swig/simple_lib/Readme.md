Building
========

Building Using distutils
-------------------------
python setup.py build_ext
python setup.py install --install-platlib=.


Building Manually
-----------------
Compile the shared library:
    g++ -fPIC -Wall -Wextra -shared mylib.cpp -o libmylib.so


Create the SWIG interface file to wrap the library
    - Located in "mylib.i"


Auto-generate wrapper code with SWIG
- Use SWIG to generate the "mylib_wrap.cxx" C++ and "mylib.py" Python extenstion module wrapper code
    swig -Wall -c++ -python mylib.i


Compile the Python module:
-Use g++ to compile the Python extension module as a shared library "_mylib.so" which is importable in Python and links to mylib.so and Python
    g++ -fPIC -Wall -Wextra -shared mylib_wrap.cxx -o _mylib.so -L. -lmylib -I/home/todd/anaconda3/include/python3.5m -L/home/todd/anaconda3/lib -lpython3.5m



Testing
=======

Running Manually
----------------
Make sure the shared objects we just built are on the library path by setting LD_LIBRARY_PATH appropriately and then just run Python

    LD_LIBRARY_PATH=. ipython

    Python 3.5.2 |Anaconda custom (64-bit)| (default, Jul  2 2016, 17:53:06)
    Type "copyright", "credits" or "license" for more information.

    IPython 5.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: import mylib

    In [2]: i = mylib.Foo()

    In [3]: mylib.bar(i)
    0x202c210

    In [4]: mylib.bar(i)
    0x202c210

    In [5]: mylib.bar(mylib.Foo())
    0x20098a0

    In [6]:


Running with test.py
--------------------
python test.py
