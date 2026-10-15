"""
This file is to obtain the area function A(xi) as an array of numbers and to plot it.
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

pi  = math.pi
num = 10000
L   = 1
V   = 1

nu = np.linspace(0, pi, num)
xi = np.zeros_like(nu)
A  = np.zeros_like(nu)

for idx in range(len(nu)):
    xi[idx] = (1/pi) * (nu[idx] - 0.5 * math.sin(2 * nu[idx]))
    A[idx]  = (4/3) * (V/L) * (math.sin(nu[idx]))**2

# Plotting A(xi) and sqrt(A(xi))
fig, ax = plt.subplots()
#ax.plot(nu, xi, 'b')
ax.plot(xi, A, 'b')
ax.plot(xi, A**0.5, linestyle='--', color='b')
x_ticks = np.linspace(0, 1, 11)
ax.set_xticks(x_ticks)
ax.legend(['A', 'A^0.5'])
ax.set_title('Area Function')
plt.show()

# Validation of area constraint, i.e., \int{A(xi)} = 1

# We can use the substitution \int{A(xi)d(xi)} = \int{A(nu)*[d(xi)/d(nu)]*d(nu)}
# Where [d(xi)/d(nu)] = (2 * (sin(nu))**2) / pi
# The boundaries then change from (0, 1) to (0, pi)

V_L = quad(lambda theta : (4/3) * (V/L) * (math.sin(theta))**2 * (2 * (math.sin(theta))**2) / pi, 0, pi)[0]
print(V_L)


