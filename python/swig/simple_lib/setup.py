from distutils.core import setup, Extension

name = "mylib"  # name of the module
version = "1.0" # the module's version number

setup(name=name, version=version,
      # distutils detects .i files and compiles them automatically
      ext_modules=[Extension(name='_mylib', # SWIG requires _ as a prefix for the module name
                             sources=["mylib.i", "mylib.cpp"],
                             include_dirs=[],
                             swig_opts=["-c++"])
    ])
