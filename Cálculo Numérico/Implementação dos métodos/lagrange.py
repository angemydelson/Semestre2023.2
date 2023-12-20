def lagrange_interpolation(x, y, xi):
    n = len(x)
    if n != len(y):
        raise ValueError("As listas de x e y devem ter o mesmo tamanho.")
    
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    
    return result

# Exemplo de uso:
x = [0, 1, 2, 3]
y = [1, 2, 3, 6]

xi = 1.5

interpolated_value = lagrange_interpolation(x, y, xi)
print(f"O valor interpolado em xi = {xi} é aproximadamente: {interpolated_value}")