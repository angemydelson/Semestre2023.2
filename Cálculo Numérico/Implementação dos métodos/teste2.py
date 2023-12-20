import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
import pandas as pd

def differential_equations(x, y):
    dydx = np.vstack((y[1], 2 * y[1] - y[0] + x * np.exp(x) - x))
    return dydx

def boundary_conditions(ya, yb):
    return np.array([ya[0], yb[0] + 4])

# Definir o intervalo
x_span = [0, 2]

# Definir a malha
x_mesh = np.arange(x_span[0], x_span[1] + 0.1, 0.1)

# Guess inicial para a solução
initial_guess = np.zeros((2, x_mesh.size))

# Resolver o PVC
solution = solve_bvp(differential_equations, boundary_conditions, x_mesh, initial_guess)

# Calcular a solução exata para comparação
x_exact = np.linspace(0, 2, 100)
y_exact = ((x_exact**3 * np.exp(x_exact))/6) - ((5 * x_exact * np.exp(x_exact))/3) + 2 * np.exp(x_exact) - x_exact - 2

# Criar um DataFrame para os resultados
df = pd.DataFrame({'x': solution.x, 'Numérico': solution.y[0], 'Exato': y_exact})

# Imprimir a tabela
print(df)

# Plotar os resultados
plt.plot(solution.x, solution.y[0], label='Numérico')
plt.plot(x_exact, y_exact, label='Exato', linestyle='--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()
