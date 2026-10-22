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

def rk4(dydx, x0, y0, x, h):
    n = (x + x0) / h
    y = y0
    for i in range(1, int(n + 1)):
        k_1 = dydx(x0, y)
        k_2 = dydx(x0 + h/2, y + k_1*h/2)
        k_3 = dydx(x0 + h/2, y + k_2*h/2)
        k_4 = dydx(x0 + h/2, y + k_3*h)

        x0 = x0 + h
        y = y + (1.0/6.0) * (k_1 + 2*k_2 + 2*k_3 + k_4)*h

    return y

