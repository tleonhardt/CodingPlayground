cmake_minimum_required(VERSION 3.4)
project("libsodium_signatures" C)

# Set compiler flags in a generic cross-platform compatible manner
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2 -Wall")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -O2 -Wall")

# Tell CMake where to look for header files
include_directories(.)

# Tell CMake where to look for libraries
link_directories(.)

set(libs sodium)

# Files to build for each executable
set(GENKEY_SRC nacl_genkey.c)
set(SIGN_SRC nacl_sign.c)
set(VERIFY_SRC nacl_verify.c)

# Executables to build
set(GENKEY_EXE nacl_keygen)
add_executable(${GENKEY_EXE} ${GENKEY_SRC})
target_link_libraries(${GENKEY_EXE} ${libs})

set(SIGN_EXE nacl_sign)
add_executable(${SIGN_EXE} ${SIGN_SRC})
target_link_libraries(${SIGN_EXE} ${libs})

set(VERIFY_EXE nacl_verify)
add_executable(${VERIFY_EXE} ${VERIFY_SRC})
target_link_libraries(${VERIFY_EXE} ${libs})
