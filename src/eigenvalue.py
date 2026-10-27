"""
We have the first order system [y, p]' = [p, -\lambda*A^(-2)*y] where p = y'
Since python does not allow lambda as a keyword, we shall use \lambda = eig
"""
from solver import rk4
from keller import area_nu
import numpy as np

def u(y, p, eig, V, L):
    A = area_nu(y, V, L)
    return -eig * A**-2 * y



solution = rk4(u, y0, p0, h, n)
