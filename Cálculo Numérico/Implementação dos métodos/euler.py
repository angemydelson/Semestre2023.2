import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, xn, y0, h):
    n = int((xn - x0) / h) + 1
    t = np.linspace(x0, xn, n)
    y = np.zeros_like(t)
    y[0] = y0
    
    for i in range(1, n):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
    
    return t, y

def f(x, y):
    return y/x - (y/x)**2

def exact(x):
    return x/(1 + np.log(x))

t, P = euler_method(f, 1, 3, 1, 0.25)
u, Q = euler_method(f, 1, 3, 1, 0.1)
v, R = euler_method(f, 1, 3, 1, 0.05)

y_values1 = exact(t)
y_values2 = exact(u)
y_values3 = exact(v)

errors_1 = np.abs(y_values1 - P)
errors_2 = np.abs(y_values2 - Q)
errors_3 = np.abs(y_values3 - R)

# plt.plot(t, errors_1, 'red', label='h = 0.25')
# plt.plot(u, errors_2, 'blue', label='h = 0.1')
# plt.plot(v, errors_3, 'green', label='h = 0.05')

plt.plot(v, y_values3, 'black', label='Analítica')
plt.plot(t, P, 'r', label='h = 0.25')
plt.plot(u, Q, 'b', label='h = 0.1')
plt.plot(v, R, 'g', label='h = 0.05')

plt.legend()
plt.grid(True)
plt.show()