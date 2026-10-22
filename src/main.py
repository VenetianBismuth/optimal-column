import matplotlib.pyplot as plt
from scipy.integrate import quad
from keller import *

pi = np.pi

def main():
    V = 1.0
    L = 1.0
    delta = 0.005
    nu = np.arange(0, np.pi, delta)
    V_L = quad(lambda theta: (4 / 3) * (V / L) * (np.sin(theta)) ** 2 * (2 * (np.sin(theta)) ** 2) / pi, 0, pi)[0]
    print(V_L)

    xi = xi_nu(nu)
    A  = area_nu(nu, V, L)
    plt.plot(xi, A, 'k')
    plt.plot(xi, np.sqrt(A), 'k--')
    plt.xlabel(r"$\xi = x/L$")
    plt.ylabel(r"$A(\xi)$")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()