#!/usr/bin/env python
""" Python wrapper to time the Cython implementation for computing the nth fibonacchi number
in a non-recursive fashion.
"""
from fib_python import compute_fibonacchi
from fib import compute_fibonacchi_cython

if __name__ == '__main__':
    import sys
    import timeit

    n = 20
    try:
        n = int(sys.argv[1])
    except Exception:
        pass

    number_of_times = 100000
    try:
        number_of_times = int(sys.argv[2])
    except Exception:
        pass

    fib_py = compute_fibonacchi(n)
    fib_cy = compute_fibonacchi_cython(n)
    if fib_py != fib_cy:
        raise(ValueError(fib_cy))

    py_tot = timeit.timeit("compute_fibonacchi({})".format(n),
                           setup="from fib_python import compute_fibonacchi",
                           number=number_of_times)
    cy_tot = timeit.timeit("compute_fibonacchi_cython({})".format(n),
                           setup="from fib import compute_fibonacchi_cython",
                           number=number_of_times)
    py_avg = py_tot / number_of_times
    cy_avg = cy_tot / number_of_times

    print("fib({}) = {}".format(n, fib_py))
    print("Python average time:  {0:.2g}".format(py_avg))
    print("Cython average time:  {0:.2g}".format(cy_avg))
    print("Cython speedup: {0:.2g} times".format(py_avg/cy_avg))
