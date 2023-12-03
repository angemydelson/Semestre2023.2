import numpy as np
import matplotlib.pyplot as plt

def quadratic_interpolation(x_values, y_values, new_x):
    # Criar uma matriz A para o sistema de equações quadráticas
    A = np.vstack([np.ones(len(x_values)), x_values, x_values**2]).T

    # Resolver o sistema de equações usando mínimos quadrados
    a, b, c = np.linalg.lstsq(A, y_values, rcond=None)[0]

    # Calcular o novo valor de y para o novo valor de x
    new_y = a + b * new_x + c * new_x**2

    return new_y, a, b, c

# Exemplo de uso
x_values = np.array([2019, 2021])
y_values = np.array([12124, 5700])
new_x = 2020

result, a, b, c = quadratic_interpolation(x_values, y_values, new_x)
print(f"Para x = {new_x}, o valor aproximado de y é: {result}")

# Plotar os dados e a curva de interpolação quadrática
plt.scatter(x_values, y_values, label='Pontos de Dados')
x_fit = np.linspace(min(x_values), max(x_values), 100)
y_fit = a + b * x_fit + c * x_fit**2
plt.plot(x_fit, y_fit, label='Interpolação Quadrática', color='red')
plt.title('Interpolação Quadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
