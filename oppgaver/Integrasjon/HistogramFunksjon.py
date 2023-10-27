import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('kai.csv', delimiter=',')


data = data[:,1].astype(int)

mu = np.mean(data)
print(mu)
sigma = np.std(data)
print(sigma)

N = np.size(data)


plt.hist(data, bins = np.linspace(151.5,159.5,9))
plt.axis([150, 160, 0, 12])
x = np.linspace(150,159,1000)
plt.savefig("kai-2")  


x = np.linspace(150,159,1000)
y = N*np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
plt.plot(x,y)

plt.savefig("kai-3")  

