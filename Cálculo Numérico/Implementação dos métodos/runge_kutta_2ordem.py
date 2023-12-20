# Python3 program to implement Runge
# Kutta method
import numpy as np
import matplotlib.pyplot as plt
 
# A sample differential equation
def f(x, y) :
    return y/x - (y/x)**2

def exact(x):
    return x/(1 + np.log(x))
 
# Finds value of y for a given x
# using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h) :
 
    # Count number of iterations
    # using step size or
    # step height h
    n = int((x - x0) / h) + 1
    t = np.linspace(x0, x, n)
    ya = np.zeros_like(t)
    ya[0] = y0

    y = y0
     
    for i in range(1, n) :
         
        # Apply Runge Kutta Formulas
        # to find next value of y
        k1 = h * f(x0, y)
        k2 = h * f(x0 + h, y + k1)

        # Update next value of y
        y = y + (1.0 / 2.0) * (k1 + k2)
        ya[i] = y
 
        # Update next value of x
        x0 = x0 + h
 
    return t, ya
 
# Driver Code
if __name__ == "__main__" :
 
    x0 = 1
    y = 1
    x = 3
    h = 0.25
 
    t, P = rungeKutta(x0, y, x, h)
    u, Q = rungeKutta(x0, y, x, 0.1)
    v, R = rungeKutta(x0, y, x, 0.05)

    y_values1 = exact(t)
    y_values2 = exact(u)
    y_values3 = exact(v)

    errors_1 = np.abs(y_values1 - P)
    errors_2 = np.abs(y_values2 - Q)
    errors_3 = np.abs(y_values3 - R)

    plt.plot(t, errors_1, 'red', label='h = 0.25')
    plt.plot(u, errors_2, 'blue', label='h = 0.1')
    plt.plot(v, errors_3, 'green', label='h = 0.05')

    # plt.plot(v, y_values3, 'black', label='Analítica')
    # plt.plot(t, P, 'r', label='h = 0.25')
    # plt.plot(u, Q, 'b', label='h = 0.1')
    # plt.plot(v, R, 'g', label='h = 0.05')

    plt.legend()
    plt.grid(True)
    plt.show()
