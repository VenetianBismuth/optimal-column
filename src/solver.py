"""
RK4 solves ODEs in the form of
    dy/dx = f(x, y), y(0) = y0.
We define a function to implement 4th order Runge-Kutta, i.e., RK4:
    y_(i+1) = y_i + (1/6) * (k_1 + 2*k_2 + 2*k_3 + k_4)*h
where
    k_1 = f(x_i, y_i)
    k_2 = f(x_i + h/2, y_i + k_1*h/2)
    k_3 = f(x_i + h/2, y_i + k_2*h/2)
    k_4 = f(x_i + h/2, y_i + k_3*h).
"""
import numpy as np

def rk4(dydx, x0, y0, h, n):
    soln = [(x0, y0)]
    x = x0
    y = y0

    for i in range(n):
        k_1 = dydx(x0, y)
        k_2 = dydx(x0 + h/2, y + k_1*h/2)
        k_3 = dydx(x0 + h/2, y + k_2*h/2)
        k_4 = dydx(x0 + h/2, y + k_3*h)

        x = x + h
        y = y + (1.0/6.0) * (k_1 + 2*k_2 + 2*k_3 + k_4)*h
        soln.append((x, y))

    return soln

def bisection(y, xl, xu, n, es):
    fl = y(xl)
    fu = y(xu)

    if np.sign(fl) == np.sign(fu): raise Exception('No sign change')
    xr = xl
    iter = 0
    ea = 100

    soln = [(iter, xl, xu, xr, ea)]
    while iter < n and ea > es:
        xr_old = xr
        xr = (xl + xu) / 2.0
        fr = y(xr)
        iter += 1

        if xr != 0: ea = abs((xr - xr_old) / xr) * 100

        if fr == 0: break
        elif np.sign(fl) == np.sign(fr):
            xl = xr
            fl = fr
        elif np.sign(fu) == np.sign(fr):
            xu = xr
            fu = fr

        soln.append((iter, xl, xu, xr, ea))

    return soln

"""
Trial
---Trial for bisection---
def f(c):
    return ((68.1 * 9.81) / c) * (1 - np.exp(-10*c / 68.1)) - 40
xl = 12
xu = 16
n = 100
es = 0.05
solution = bisection(f, xl, xu, n, es)
print(solution)

---Trial for RK4---
import matplotlib.pyplot as plt
def f(x, y):
    return 2*x*y + 5*y

x0 = 0.0
y0 = 50.0
h = 0.01
n = 1000

solution = rk4(f, x0, y0, h, n)
xval = [x for x, _ in solution]
yval = [y for _, y in solution]

plt.plot(xval, yval, label='y(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trial')
plt.legend()
plt.grid(True)
plt.show()

In this trial, we have the system [x, y]' = [1, 2xy + 5y]
"""