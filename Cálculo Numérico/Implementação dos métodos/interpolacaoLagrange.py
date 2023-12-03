# Lagrange Interpolation

# Importing NumPy Library
import numpy as np

# Reading number of unknowns
#n = int(input('Enter number of data points: '))


x = np.array([2019, 2021])
y = np.array([12124, 5700])

# Reading data points
""" print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']=')) """


# Reading interpolation point
xp = 2020

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(len(x)):
    
    p = 1
    
    for j in range(len(x)):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))