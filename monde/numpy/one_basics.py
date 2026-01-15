import numpy as np
import timeit as timeit


rng = np.random.default_rng(seed=13)



arrayen = rng.choice(
    500,
    (2, 2, 4),
    replace=False
)



print("- - - - - - ")


print(arrayen)

print(arrayen[1, 1, 1])
print(arrayen[[[0, 0, 0]]])


