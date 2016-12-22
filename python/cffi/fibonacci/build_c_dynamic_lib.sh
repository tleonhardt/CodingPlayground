# Compile with position-independent code
gcc -c -Wall -Werror -g0 -O3 -fpic fibonacci.c

# Create a shared library from an object file
gcc -shared -o libfibonacci.so fibonacci.o
