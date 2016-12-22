from distutils.core import setup, Extension

name = "fibonacci"  # name of the module
version = "1.0"     # the module's version number

setup(name=name, version=version,
      # distutils detects .i files and compiles them automatically
      ext_modules=[Extension(name='_{}'.format(name), # SWIG requires _ as a prefix for the module name
                             sources=["fibonacci.i", "fibonacci.c"],
                             include_dirs=[],
                             swig_opts=[])
    ])
