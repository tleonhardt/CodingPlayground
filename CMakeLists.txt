cmake_minimum_required(VERSION 3.9)
project(CodingPlayground)

set(CMAKE_CXX_STANDARD 11)

add_executable(CodingPlayground
        c/ansi_color/AnsiColorCodes.h
        c/ansi_color/hello_color.c
        c/compression/hello_zstandard.c
        c/crypto/nacl_genkey.c
        c/crypto/nacl_sign.c
        c/crypto/nacl_verify.c
        cpp/zlog/t_zlog.cpp
        python/cffi/fibonacci/fibonacci.c
        python/cffi/fibonacci/fibonacci.h
        python/cython/fibonacci/fib.c
        python/cython/fibonacci_wrapper/fibonacci.c
        python/cython/fibonacci_wrapper/fibonacci.h
        python/cython/hello/hello.c
        python/swig/cmake/example.cpp
        python/swig/cmake/example.h
        python/swig/cmake/example.i
        python/swig/cpp_code/src/HelloWorld.cpp
        python/swig/cpp_code/src/HelloWorld.h
        python/swig/cpp_code/src/HelloWorld2.cpp
        python/swig/cpp_code/src/HelloWorld2.h
        python/swig/cpp_code/helloworld.i
        python/swig/fibonacci/fibonacci.c
        python/swig/fibonacci/fibonacci.h
        python/swig/fibonacci/fibonacci.i
        python/swig/fibonacci/fibonacci_wrap.c
        python/swig/simple_lib/mylib.cpp
        python/swig/simple_lib/mylib.h
        python/swig/simple_lib/mylib.i
        python/swig/tutorial/example.c
        python/swig/tutorial/example.h
        python/swig/tutorial/example.i)
