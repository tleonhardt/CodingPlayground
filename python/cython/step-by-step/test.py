import statistics
import random

a = statistics.StatisticalArray()
a.append(random.random())
a.append(random.random())
a.append(random.random())
a.append(random.random())

b = statistics.StatisticalArray()
b.append(random.random())
b.append(random.random())
b.append(random.random())
b.append(random.random())

pc = a.pearson_coefficient(b)
print("a.pearson_coefficient(b) = {}".format(pc))
