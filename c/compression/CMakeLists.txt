cmake_minimum_required(VERSION 3.4)
project("compression" C)

# Set compiler flags in a generic cross-platform compatible manner
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2 -Wall")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -O2 -Wall")

# Tell CMake where to look for header files
include_directories(.)

# Tell CMake where to look for libraries
link_directories(.)

set(zstd zstd)

# Files to build for each executable
set(HELLO_ZSTD_SRC hello_zstandard.c)

# Executables to build
set(HELLO_ZSTD_EXE hello_zstandard)
add_executable(${HELLO_ZSTD_EXE} ${HELLO_ZSTD_SRC})
target_link_libraries(${HELLO_ZSTD_EXE} ${zstd})
