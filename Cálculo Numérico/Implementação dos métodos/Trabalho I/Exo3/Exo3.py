import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from matplotlib.backends.backend_pdf import PdfPages


# Função que representa a equação diferencial y' = y/x - y^2/x^2
def differential_equation(x, y):
    return y/x - (y/x)**2

# Função que implementa o método de Euler
def euler_method(f, x0, y0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]

    for i in range(1, len(x_values)):
        x = x_values[i - 1]
        y = y_values[i - 1]
        y_new = y + h * f(x, y)
        y_values.append(y_new)

    return x_values, y_values

# Solução analítica
def analytical_solution(x):
    return x / (1 + np.log(x))

# Parâmetros do problema
x0 = 1
y0 = 1

# a. Resolvendo para h = 0.25, h = 0.1 e h = 0.05
h_values = [0.25, 0.1, 0.05]
plt.figure(figsize=(10, 6))

for h in h_values:
    x_values, y_values = euler_method(differential_equation, x0, y0, h, 3)
    plt.plot(x_values, y_values, label=f'Método de Euler (h={h})')

# b. Plotando a solução analítica
x_analytical = np.linspace(1, 3, 100)
y_analytical = analytical_solution(x_analytical)
plt.plot(x_analytical, y_analytical, label='Solução Analítica', linestyle='--', color='black')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução Aproximada pelo Método de Euler vs Solução Analítica')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))

for h in h_values:
    x_values, y_values = euler_method(differential_equation, x0, y0, h, 3)
    analytical_values = analytical_solution(x_values)
    absolute_errors = np.abs(y_values - analytical_values)
    plt.plot(x_values, absolute_errors, label=f'Erro (h={h})')

plt.xlabel('x')
plt.ylabel('Erro Absoluto')
plt.title('Erros Absolutos em Função de x')
plt.legend()
plt.grid(True)
plt.show()

results_table = []

for h in h_values:
    x_values, y_values = euler_method(differential_equation, x0, y0, h, 3)
    analytical_values = analytical_solution(x_values)
    absolute_errors = np.abs(y_values - analytical_values)
    max_absolute_error = np.max(absolute_errors)

    results_table.append([f'Método de Euler (h={h})', max_absolute_error])

# Convertendo a tabela para um DataFrame pandas
df = pd.DataFrame(results_table, columns=['Método', 'Erro Máximo'])

# Exibindo a tabela formatada
print(tabulate(df, headers='keys', tablefmt='pretty'))

# Salvando a tabela como PDF
with PdfPages('resultados.pdf') as pdf:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    pdf.savefig(fig, bbox_inches='tight')

# Exibindo a tabela no console
print("Tabela de Resultados:")
print(tabulate(df, headers='keys', tablefmt='pretty'))

print("Resultados salvos em 'resultados.pdf'")
