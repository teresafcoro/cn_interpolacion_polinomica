import numpy as np
import matplotlib.pyplot as plt

def chebyshev(f, a, b, n):
    # nodos equiespaciados que incluyen los extremos del intervalo
    xe = np.linspace(a, b, n)
    # polinomio nodos equiespaciados
    pe = np.polyfit(xe, f(xe), n-1)
    
    x = np.linspace(a, b, 500)
    plt.figure()   
    plt.plot(x, f(x), 'b', label = u'función')
    plt.plot(xe, f(xe), 'ro', label = 'nodos')
    plt.plot(x, np.polyval(pe ,x), 'r', label = 'polinomio')
    plt.title('Nodos equiespaciados')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend(loc = 'best')
    plt.show()
    
    # nodos chebyshev en [-1, 1]
    i = np.arange(1, n+1) # i = 1, 2, ..., n
    xc = np.cos(((2.*i - 1)*np.pi)/(2.*n))
    # polinomio nodos chebyshev
    pc = np.polyfit(xc, f(xc), n-1)

    plt.figure() 
    plt.plot(x, f(x), 'b', label = u'función')
    plt.plot(xc, f(xc), 'ro', label = 'nodos')
    plt.plot(x, np.polyval(pc, x), 'r', label = 'polinomio')
    plt.title('Nodos Chebyshev')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend(loc = 'upper center')
    plt.show()

# interpola la función f en [a, b] utilizando n nodos:
f = lambda x: 1/(1 + 25*x**2) ; a = -1.; b =  1.; n = 11  
chebyshev(f, a, b, n)

f = lambda x: np.exp(-20*x**2) ; a = -1.; b =  1.; n = 15
chebyshev(f, a, b, n)
