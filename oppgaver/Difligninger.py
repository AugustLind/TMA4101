import numpy as np
import matplotlib.pyplot as plt

def x(t,a,k,x0):
    return (k*x0*np.exp(a*t)/(k-x0+x0*np.exp(a*t)))

x_verdier = []
y_verdier = []

a = 0.2
k = 5
x0 = 1
xStopp = 100
x1 = 0

while x1 <= xStopp:
    y_verdier.append(x(x1,a,k,x0))
    x_verdier.append(x1)
    x1 += 0.01

plt.plot(x_verdier,y_verdier)
plt.show()