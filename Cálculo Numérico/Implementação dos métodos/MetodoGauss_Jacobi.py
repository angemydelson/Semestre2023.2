import numpy as np
import pandas as pd

def gauss_jacobi(A, b, tolerancia, iteracoes_maximas=50):
    """
    Resolve um sistema linear Ax = b usando o método de Gauss-Jacobi.

    Parâmetros:
    A (numpy.ndarray): Matriz dos coeficientes do sistema.
    b (numpy.ndarray): Vetor do lado direito do sistema.
    tolerancia (float): Tolerância para o critério de parada.
    iteracoes_maximas (int): Número máximo de iterações.

    Retorna:
    resultados (pandas.DataFrame): DataFrame com os resultados de cada iteração.
    """

    n = len(b)
    x = np.zeros(n)  # Inicialização da solução
    resultados = []

    for k in range(iteracoes_maximas):
        x_anterior = x.copy()

        for i in range(n):
            soma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x_anterior[i + 1:])
            x[i] = (b[i] - soma) / A[i, i]

        # Critério de parada
        erro_relativo = np.linalg.norm(x - x_anterior, np.inf) / np.linalg.norm(x, np.inf)
        
        # Adicionar resultados à lista
        resultados.append([k + 1, x.copy(), round(erro_relativo, 5)])

        if erro_relativo < tolerancia:
            break

    # Criar DataFrame usando pandas
    colunas = ['Iteração', 'Solução', 'Erro Relativo']
    resultados_df = pd.DataFrame(resultados, columns=colunas)

    return resultados_df

# Exemplo de sistema linear
A = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]])

b = np.array([7, -8, 6])

# Defina a tolerância desejada
tolerancia = 0.05

# Resolvendo o sistema usando Gauss-Jacobi
resultados_iteracoes = gauss_jacobi(A, b, tolerancia)

# Configurar pandas para exibir apenas 5 casas decimais
pd.set_option('display.float_format', '{:.5f}'.format)

# Imprimir todas as iterações
print(resultados_iteracoes)
