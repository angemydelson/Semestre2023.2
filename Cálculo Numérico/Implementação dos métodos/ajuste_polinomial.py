import numpy as np

def ajuste_polinomial(x, y, grau):
    X = np.vander(x, grau + 1, increasing=True)

    coeficientes = np.linalg.lstsq(X, y, rcond=None)[0]

    return coeficientes

def avaliar_polinomio(coeficientes, x):
    return np.polyval(coeficientes, x)

# Pontos de exemplo
x = np.array([-2, -1.5, 0, 1, 2.2, 3.1])
y = np.array([-30.5, -20.5, -3.3, 8.9, 16.8, 21.4])

# Grau do polinômio
grau = 2

coeficientes = ajuste_polinomial(x, y, grau)

print(f"Coeficientes do polinômio de grau {grau}: {coeficientes}")