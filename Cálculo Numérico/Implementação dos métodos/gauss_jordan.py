import numpy as np

def gauss_jordan_elimination(A, B):
    n = len(B)
    
    # Construir a matriz aumentada [A | B]
    augmented_matrix = np.column_stack((A, B))
    
    for i in range(n):
        # Normalizar a linha i
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        
        # Eliminação para trás
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # As soluções estão na última coluna da matriz aumentada
    solutions = augmented_matrix[:, -1]

    return solutions

# Exemplo de uso:
A = np.array([[2, -1, 1],
              [1, 3, 2],
              [3, 2, 4]])

B = np.array([2, 10, 12])

solutions = gauss_jordan_elimination(A, B)
print("As soluções são:", solutions)
