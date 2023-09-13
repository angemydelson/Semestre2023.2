# Importar a biblioteca PrettyTable para criar tabelas organizadas
from prettytable import PrettyTable

# Função que executa o método da bissecção e gera uma tabela com resultados
def bisection_table(f, a, b, tol, max_iter):
    # Verificar se a função possui raiz no intervalo [a, b]
    if f(a) * f(b) >= 0:
        print("A função não satisfaz a condição de existência de raiz no intervalo.")
        return None
    
    # Criar uma tabela com colunas definidas
    table = PrettyTable()
    table.field_names = ["Iteração", "a", "b", "c", "f(a)", "f(b)", "f(c)", "f(a) * f(c)", "Tamanho do Intervalo"]
    
    # Loop para executar o método da bissecção
    for i in range(max_iter):
        # Calcular o ponto médio do intervalo atual
        c = (a + b) / 2
        # Avaliar a função nos pontos a, b e c
        f_a = f(a)
        f_b = f(b)
        f_c = f(c)
        # Calcular o produto f(a) * f(c)
        f_a_times_f_c = f_a * f_c
        # Calcular o tamanho do intervalo
        interval_size = b - a
        
        # Adicionar uma linha à tabela com os valores calculados
        table.add_row([i+1, a, b, c, f_a, f_b, f_c, f_a_times_f_c, interval_size])
        
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
max_iterations = 100  # Número máximo de iterações

# Chamada da função para criar a tabela de bissecção
root_approx = bisection_table(example_function, a, b, tolerance, max_iterations)
