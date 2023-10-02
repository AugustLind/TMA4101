import numpy as np
import matplotlib.pyplot as plt
T=20
N=2000
h=T/N

t=np.linspace( 0 ,T,N+1)
x=np.zeros(N+1)
y=np.zeros(N+1)
x[0]= 2
y[0]= 2
my = 2

for n in range(N):
    x[n+1]=x[n]+h * (y[n])
    y[n+1]=y[n]+h * (-my*(x[n+1]**2-1)*y[n]-x[n+1])
plt.plot(t,x)
plt.plot (t,y)
plt.savefig("vanDerPol-tid.png")
            
plt.figure()
plt.plot(x,y)
plt.savefig("vanDerPol-fase.png")       