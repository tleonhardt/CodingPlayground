/** Implementation file for C++ shared library
  *
  */
#include "mylib.h"
#include <iostream>

void bar(const Foo& f)
{
    std::cout << &f << std::endl;
}
