def gregory_newton_interpolation(x, y, xi):
    n = len(x)
    if n != len(y):
        raise ValueError("As listas de x e y devem ter o mesmo tamanho.")
    
    # Inicializa uma matriz de diferenças divididas finitas
    fdd = [[0] * n for _ in range(n)]
    for i in range(n):
        fdd[i][0] = y[i]
    
    # Calcula as diferenças divididas finitas
    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (x[i+j] - x[i])
    
    # Calcula o polinômio interpolador usando a fórmula de Gregory-Newton
    result = fdd[0][0]
    factor = 1
    for j in range(1, n):
        factor *= (xi - x[j-1])
        result += fdd[0][j] * factor
    
    return result

# Exemplo de uso:
x = [8, 12, 16, 20]
y = [18, 23, 26, 21]
xi = 17

interpolated_value = gregory_newton_interpolation(x, y, xi)
print(f"O valor interpolado em xi = {xi} é aproximadamente: {interpolated_value}")
