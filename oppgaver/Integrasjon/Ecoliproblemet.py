import numpy as np
import matplotlib.pyplot as plt
#Heuns metode

T=5
N=100
h=T/N
t=np.linspace(0,T,N+1)

x=np.zeros(N+1)
x[0]=1

def f(x):
    return x

for i in range(N):
    x[i+1] = x[i] + (h/2)*(f(x[i]) + f(x[i]+h*f(x[i])))

plt.plot(t,x)
plt.show()

