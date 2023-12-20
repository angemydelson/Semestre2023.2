import numpy as np
import pandas as pd

def funcao(x, y, yp):
    return 2*yp - y + x*np.exp(x) - x

def metodo_euler(intervalo, y0, yp0, h):
    x_vals = np.arange(intervalo[0], intervalo[1] + h, h)
    y_vals = []

    y = y0
    yp = yp0

    for x in x_vals:
        y_vals.append(y)

        y_next = y + h * yp
        yp_next = yp + h * funcao(x, y, yp)

        y = y_next
        yp = yp_next

    return x_vals, y_vals

def solucao_exata(x):
    return ((x**3*np.exp(x))/6) - ((5*x*np.exp(x))/3) + 2*np.exp(x) - x - 2

# Condições iniciais
intervalo = [0, 2]
y0 = 0
yp0 = -4  # Supomos y'(0) = 0
h = 0.1

# Método de Euler
x_vals, y_vals = metodo_euler(intervalo, y0, yp0, h)

# Solução exata para comparação
solucao_exata_vals = [solucao_exata(x) for x in x_vals]

# Criar DataFrame apenas com x e y aproximados
df = pd.DataFrame({
    'x': x_vals,
    'y_aproximado': y_vals,
    'y_exato': solucao_exata_vals
})

# Exibir a tabela
print(df)
