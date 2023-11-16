import numpy as np
import sympy as sp

def elipse(x, r1, r2):
    return np.sqrt(r1**2 - (r1**2 * (x**2/r2**2)))

r1 = 2
r2 = 1
a = -1
b = 1
n = 100000
bredde = (b - a) / n
integral = 0

def derivate(f, x):
    return sp.diff(f, x)

for i in range(n):
    x = a + i * bredde
    integral += np.sqrt(1 +(elipse(x, r1, r2), x))**2 * bredde

print(integral * 2)
