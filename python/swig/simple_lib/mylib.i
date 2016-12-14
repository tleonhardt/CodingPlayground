/** SWIG interface to wrap the library
  *
  */
// Module name
%module mylib

// Make mylib_wrap.cxx include this header:
%{
#include "mylib.h"
%}

// Make SWIG look into this header:
%include "mylib.h"
