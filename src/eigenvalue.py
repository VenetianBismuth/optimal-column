"""
We have the first order system [y, p]' = [p, -\lambda*A^(-2)*y] where p = y'
Since python does not allow lambda as a keyword, we shall use \lambda = lam
"""
from solver import rk4
from solver import bisection
from keller import area_nu
import numpy as np

def u(y, p, lam, V, L):
    A = area_nu(y, V, L)
    return -lam * A**-2 * y

def residual(lam, q, n):
    def dydx(x, state):
        y, p = state
        return (p, -lam * q(x) * y)

    solution = rk4(dydx, x0 = 0.0, y0 = (0.0, 1.0), h = 0.01, n = n)

    y_end = solution[-1][1]
    return y_end[0]

def func(lam):
    return residual(lam, q, n = 200)

eigenvalue = bisection(func, 1.0, 30.0, n = 100, es = 0.01)
print(eigenvalue)