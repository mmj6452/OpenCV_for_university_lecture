import numpy as np
import matplotlib.pyplot as plt
import math

def exp(knN):
    th = -2*math.pi*knN
    return complex(math.cos(th), math.sin(th))


def dft(g):
    N = len(g)
    dst = [sum(g[n]*exp(k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst)

def idft(g):
    N = len(g)
    dst = [sum(g[n]*exp(-k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst)/N

fmax = 1000
dt = 1/fmax*2
t = np.arange(0, 1, dt)

g1 = np.sin(2*np.pi * t * 50)
g2 = np.sin(2*np.pi * t * 120)
g3 = np.sin(2*np.pi * t * 260)
g = 0.6*g1 + 0.9*g2 + 0.2*g3

N = len(g)
df = fmax/N
f = np.arange(0, fmax, df)
xf = dft(g) * dt
g2 = idft(xf)/dt

plt.figure(figsize=(10,10))
plt.subplot(3,1,1),plt.plot(t[0:200],g[0:200]),plt.title('g')
plt.subplot(3,1,2),plt.plot(f,np.abs(xf)),plt.title('xf')
plt.subplot(3,1,3),plt.plot(t[0:200],g2[0:200]),plt.title('g2')
plt.show()