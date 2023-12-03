# Importar a biblioteca PrettyTable para criar tabelas organizadas
from prettytable import PrettyTable

# Função que executa o método das posições falsas e gera uma tabela com resultados
def false_position_table(f, a, b, tol, max_iter):
    # Verificar se a função possui raiz no intervalo [a, b]
    if f(a) * f(b) >= 0:
        print("A função não satisfaz a condição de existência de raiz no intervalo.")
        return None
    
    # Criar uma tabela com colunas definidas
    table = PrettyTable()
    table.field_names = ["Iteração", "x", "f(x)", "b-a"]
    
    # Loop para executar o método das posições falsas
    for i in range(max_iter):
        # Calcular o ponto c pela fórmula do método das posições falsas
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        # Avaliar a função no ponto c
        f_c = f(c)
        # Calcular o tamanho do intervalo
        interval_size = b - a
        
        # Adicionar uma linha à tabela com os valores calculados, formatando para 6 dígitos após a vírgula
        table.add_row([
            i+1,
            round(c, 6),
            round(f_c, 6),
            round(interval_size, 6)
        ])
        
        # Verificar se a raiz foi encontrada com a tolerância especificada
        if abs(f_c) < tol:
            print("Raiz aproximada encontrada!")
            print(table)
            return c
        
        # Atualizar os limites do intervalo de acordo com o sinal de f(c)
        if f_c * f(a) < 0:
            b = c
        else:
            a = c
            
    # Mostrar mensagem caso o método não encontre a raiz
    print("Não foi possível encontrar uma raiz após todas as iterações.")
    print(table)
    return None

# Função de exemplo
def example_function(x):
    return x**3 - x*9 + 3

# Intervalo [a, b] onde a função tem raiz
a = 0
b = 1

# Tolerância e número máximo de iterações
tolerance = 10**-3  # Tolerância definida
max_iterations = 20  # Número máximo de iterações

# Chamada da função para criar a tabela de posições falsas
root_approx_false_position = false_position_table(example_function, a, b, tolerance, max_iterations)
