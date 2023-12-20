import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])  # Valores de x
y = np.array([3, 6, 8, 12, 14])  # Valores de y correspondentes

# Calcular os coeficientes da regressão linear (ajuste linear)
m, b = np.polyfit(x, y, 1)  # Ajuste de uma reta de primeira ordem (grau 1)

# Calcular os valores previstos (regressão) usando os coeficientes encontrados
y_pred = m * x + b

# Plotar os dados e a linha de regressão
plt.scatter(x, y, label='Dados')  # Plotar os pontos de dados
plt.plot(x, y_pred, color='red', label='Regressão Linear')  # Plotar a linha de regressão
plt.title('Ajuste Linear de Curvas (Regressão Linear)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir os coeficientes da regressão
print(f"Coeficiente angular (inclinação): {m}")
print(f"Coeficiente linear (interceptação): {b}")
