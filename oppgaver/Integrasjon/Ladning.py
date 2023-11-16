import numpy as np 

t0 = 1 # Ampere
R = 1 # Ohm
C = 1 # Farad

def strom(t):
    return t0 * np.exp(-t / (R * C))

t = np.linspace(0, int(1e6), int(1e7))
total_charge = 0
for i in range(len(t)):
    if strom(t[i]) < 1e-10:
        break
    total_charge += strom(t[i])

print(f"Total ladning gjennom motstanden: {total_charge:.2f} C")