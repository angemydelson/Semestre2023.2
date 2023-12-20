from scipy.integrate import quad
import numpy as np

def calcular_integral(funcao, limite_inferior, limite_superior, metodo):
    resultado, erro = quad(funcao, limite_inferior, limite_superior, method=metodo)
    return resultado, erro

def imprimir_resultados(resultado, erro, metodo):
    print(f"Resultado usando a regra {metodo}:")
    print(f"Integral aproximada: {resultado}")
    print(f"Erro estimado: {erro}")
    print()

# Função exponencial
def funcao(x):
    return np.exp(x)

# Definir limites de integração
limite_inferior = 0
limite_superior = 1

# Calcular integral usando a regra dos trapézios
resultado_trapezios, erro_trapezios = calcular_integral(funcao, limite_inferior, limite_superior, 'trapezoid')

# Calcular integral usando a regra de Simpson
resultado_simpson, erro_simpson = calcular_integral(funcao, limite_inferior, limite_superior, 'simpson')

# Imprimir os resultados
imprimir_resultados(resultado_trapezios, erro_trapezios, 'dos trapézios')
imprimir_resultados(resultado_simpson, erro_simpson, 'de Simpson')
