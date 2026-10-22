"""
This file is to obtain the area function A(xi) as an array of numbers and to plot it.
"""

import numpy as np


pi  = np.pi
"""
num = 10000
L   = 1
V   = 1

nu = np.linspace(0, pi, num)
xi = np.zeros_like(nu)
A  = np.zeros_like(nu)

for idx in range(len(nu)):
    xi[idx] = (1/pi) * (nu[idx] - 0.5 * np.sin(2 * nu[idx]))
    A[idx]  = (4/3) * (V/L) * (np.sin(nu[idx]))**2
"""

def xi_nu(nu):
    return (1/pi) * (nu - 0.5 * np.sin(2 * nu))

def area_nu(nu, V, L):
    return (4/3) * (V/L) * (np.sin(nu))**2


