import numpy as np
import timeit as timeit

print(timeit.timeit("np.sort([1, 4, 5, 8, 10, 4])", globals=globals(), number=10))



