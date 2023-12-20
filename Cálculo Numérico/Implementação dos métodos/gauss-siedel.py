import numpy as np

def gauss(A, b, x, n):
    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    print(f"A solução aproximada após {n} iterações é: {x}")

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]]) #cada matriz é uma linha
b = [1.0, 2.0, 3.0]
x = [1, 1, 1] #CHUTE INICIAL

n = 20 #número de iterações

gauss(A, b, x, n)