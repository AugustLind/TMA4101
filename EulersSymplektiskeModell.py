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
f = np.zeros(N+1)

for n in range(N):
    f[n]= (x[n] + y[n] - np.log(abs(x[n])) - np.log(abs(y[n])))
    x[n+1]=x[n]+h * x[n]*(1-y[n])
    y[n+1]=y[n]+h * y[n]*(x[n+1]-1)
    

plt.plot(t,x)
plt.plot (t,y)
plt.savefig("lotkavolterra-tidSymplektisk.png")

plt.plot(t,f)
plt.savefig("z.png")

            
plt.figure( )
plt.plot(x,y)
plt.savefig("lotkavolterra-faseSymplektisk.png")

