import numpy as np
import matplotlib.pyplot as plt

# Polinomios fundamentales de Lagrange


def lagrange_fund(k, x, z):
    n = len(x)
    yz = 1.
    for i in range(n):
        if k != i:
            yz *= (z - x[i]) / (x[k] - x[i])
    return yz


def polinomio_lagrange(x, y, z):
    n = len(x)
    yz = 0.
    for k in range(n):
        yz += y[k] * lagrange_fund(k, x, z)
    return yz


x = np.array([-1., 0, 2, 3, 5])
y = np.array([1., 3, 4, 3, 1])
z = np.linspace(min(x), max(x), 100)
yz = polinomio_lagrange(x, y, z)
plt.figure()
plt.plot(x, y, 'ro', label='puntos')
plt.plot(z, yz, label='Polinomio')
plt.legend()
plt.show()

x = np.array([-1., 0, 2, 3, 5, 6, 7])
y = np.array([1., 3, 4, 3, 2, 2, 1])
z = np.linspace(min(x), max(x), 100)
yz = polinomio_lagrange(x, y, z)
plt.figure()
plt.plot(x, y, 'ro', label='Puntos')
plt.plot(z, yz, label='Polinomio')
plt.legend()
plt.show()
