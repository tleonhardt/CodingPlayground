""" Cython implementation for computing the nth fibonacchi number in a
non-recursive fashion.
"""

cpdef int compute_fibonacchi_cython(int n):
    cdef int a, b, intermediate, x
    a, b = 1, 1
    for x in range(n):
        intermediate = a
        a = a + b
        b = intermediate
    return a
