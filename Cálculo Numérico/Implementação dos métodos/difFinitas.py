def forward_difference(x_values, y_values, new_x):
    n = len(x_values)
    
    # Encontrar o índice mais próximo no qual calcular a diferença para frente
    index = min(range(n), key=lambda i: abs(x_values[i] - new_x))
    
    # Verificar se o índice não está no extremo direito da lista
    if index < n - 1:
        # Calcular a diferença para frente
        h = x_values[index + 1] - x_values[index]
        forward_diff = (y_values[index + 1] - y_values[index]) / h
        
        # Calcular o novo valor de y usando a diferença para frente
        new_y = y_values[index] + forward_diff * (new_x - x_values[index])
        
        return new_y
    else:
        print("O novo valor de x está além do alcance da lista fornecida.")

# Exemplo de uso
x_values = [8, 12, 16, 20]
y_values = [18, 23, 26, 21]
new_x = 17

result = forward_difference(x_values, y_values, new_x)
print(f"Para x = {new_x}, o valor aproximado de y é: {result}")
