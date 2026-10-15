import math
import matplotlib.pyplot as plt
from scipy.integrate import quad
import area

if __name__ == "__main__":
    V_L = quad(lambda theta: (4 / 3) * (V / L) * (math.sin(theta)) ** 2 * (2 * (math.sin(theta)) ** 2) / pi, 0, pi)[0]
    print(V_L)

    fig, ax = plt.subplots()
    # ax.plot(nu, xi, 'b')
    ax.plot(xi, A, 'b')
    ax.plot(xi, A ** 0.5, linestyle='--', color='b')
    x_ticks = np.linspace(0, 1, 11)
    ax.set_xticks(x_ticks)
    ax.legend(['A', 'A^0.5'])
    ax.set_title('Area Function')
    plt.show()