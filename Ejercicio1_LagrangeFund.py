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

# Versión 1
# k = índice el polinomio fundamental
k = 2
# x = nodos
x = np.array([-1., 0, 2, 3, 5])
# z = punto donde calcular los valores del polinomio
z = 1.3
# valor del k-ésimo polinomio fundamental correspondiente a los nodos x en el punto z
yz = lagrange_fund(k, x, z)
print(yz)

# Versión 2
z = np.array([1.3, 2.1, 3.2])
yz = lagrange_fund(k, x, z)
print(yz)

# Dibujar:
z = np.linspace(min(x), max(x), 100)
y = np.eye(len(x)) # matriz identidad
for i in range(len(x)): 
    yz = lagrange_fund(i, x, z)
    plt.figure()
    plt.plot(z, yz)
    plt.plot(x, y[i], 'o')
    plt.plot(z, 0*z, 'k-')
    plt.title('L' + str(i), fontsize = 18)    
    plt.show()
