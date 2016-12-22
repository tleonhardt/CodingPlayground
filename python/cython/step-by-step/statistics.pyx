from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free

cdef extern from "string.h":
    void *memcpy(void *str1, const void *str2, size_t n)

cdef class StatisticalArray:
    cdef double* values
    cdef int num_values
    cdef max_values

    def __cinit__(StatisticalArray self, StatisticalArray copy_from=None, *pargs, **kwargs):
        if copy_from:
            self.num_values = copy_from.num_values
            self.max_values = copy_from.max_values
            self.values = <double*> PyMem_Malloc(copy_from.max_values * sizeof(double))
            memcpy(self.values, copy_from.values, copy_from.num_values * sizeof(double))
        else:
            self.values = NULL
            self.num_values = 0
            self.max_values = 0

    def __dealloc__(StatisticalArray self):
        if self.values != NULL:
            PyMem_Free(self.values)

    def __iter__(StatisticalArray self):
        cdef int index
        for index in range(self.num_values):
            yield self.values[index]

    def __getitem__(StatisticalArray self, int index):
        if index < 0:
            index = index + self.num_values

        if index < 0 or index >= self.num_values:
            raise IndexError(index)

        return self.values[index]

    def __setitem__(StatisticalArray self, int index, double value):
        if index < 0:
            index = index + self.num_values

        if index < 0 or index >= self.num_values:
            raise IndexError(index)

        self.values[index] = value

    cpdef append(StatisticalArray self, double value):
        if self.num_values == self.max_values:
            self.max_values = self.max_values * 2 if self.max_values > 0 else 8
            self.values = <double*> PyMem_Realloc(self.values, self.max_values * sizeof(double))

        self.values[self.num_values] = value

        self.num_values += 1

    cpdef double mean(StatisticalArray self):
        cdef int index
        cdef double total = 0.0

        for index in range(self.num_values):
            total += self.values[index]

        return total / self.num_values

    cpdef double variance(StatisticalArray self):
        cdef StatisticalArray temp = StatisticalArray()
        cdef double mean = self.mean()
        cdef int index

        for index in range(self.num_values):
            temp.append((self.values[index] - mean)**2)

        return temp.mean()

    cpdef double covariance(StatisticalArray self, StatisticalArray other) except? -200.0:
        if self.num_values != other.num_values:
            raise ValueError("Array sizes differ")

        cdef StatisticalArray temp = StatisticalArray()
        cdef double self_mean = self.mean()
        cdef double other_mean = other.mean()
        cdef int index

        for index in range(self.num_values):
            temp.append((self.values[index] - self_mean) * (other.values[index] - other_mean))

        return temp.mean()

    cpdef double standard_deviation(StatisticalArray self):
        return self.variance() ** 0.5

    cpdef double pearson_coefficient(StatisticalArray self, StatisticalArray other) except? -200.0:
        return self.covariance(other) / (self.standard_deviation() * other.standard_deviation())
