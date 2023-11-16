import numpy as np 

#deriverte av sinus er cosinus
def f(x):
    return np.cos(x)

a = 0
b = np.pi
n = 10000
h = (b-a)/n

integral = 0

for i in range(n):
    x0 = a + i*h
    integral += np.sqrt(1 + (f(x0)**2))*h

print(integral)

integral = 0

for i in range(n):
    x0 = a + i*h
    x1 = a + (i+1)*h
    integral += np.sqrt(1 + ((f(x0) + f(x1))*h/2))

