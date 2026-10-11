import math
import matplotlib.pyplot as plt
import numpy as np

pi = math.pi
num = 10000
L  = 1
V  = 1

nu = np.linspace(0, pi, num)
xi = np.zeros_like(nu)
A  = np.zeros_like(nu)

for idx in range(len(nu)):
    xi[idx] = (1/pi) * (nu[idx] - 0.5 * math.sin(2 * nu[idx]))
    A[idx]  = (4/3) * (V/L) * (math.sin(nu[idx]))**2


fig, ax = plt.subplots()
#ax.plot(nu, xi, 'b')
ax.plot(xi, A, 'b')
ax.plot(xi, A**0.5, linestyle='--', color='b')
x_ticks = np.linspace(0, 1, 11)
ax.set_xticks(x_ticks)
ax.legend(['A', 'A^0.5'])
plt.show()



