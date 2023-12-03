import sympy as sp
from prettytable import PrettyTable

def newton_method_table(f, x0, tol, max_iter):
    # Definir a variável simbólica
    x = sp.symbols('x')

    # Calcular a derivada da função
    f_prime = sp.diff(f, x)

    # Converter a expressão para uma função lambda
    f_lambda = sp.lambdify(x, f, modules=['numpy'])
    f_prime_lambda = sp.lambdify(x, f_prime, modules=['numpy'])

    # Criar uma tabela com colunas definidas
    table = PrettyTable()
    table.field_names = ["Iteração", "x", "f(x)", "f'(x)", "x - f(x)/f'(x)", "Tamanho do Intervalo"]

    # Loop para executar o método de Newton
    for i in range(max_iter):
        # Calcular os valores da função e de sua derivada no ponto x
        f_x = f_lambda(x0)
        f_prime_x = f_prime_lambda(x0)

        # Calcular o próximo ponto x usando a fórmula do método de Newton
        x1 = x0 - f_x / f_prime_x

        # Calcular o tamanho do intervalo
        interval_size = abs(x1 - x0)

        # Adicionar uma linha à tabela com os valores calculados
        table.add_row([i + 1, round(x0, 6), round(f_x, 6), round(f_prime_x, 6), round(x1, 6), round(interval_size, 6)])

        # Verificar se a raiz foi encontrada com a tolerância especificada
        if abs(f_x) < tol:
            print("Raiz aproximada encontrada!")
            print(table)
            return x0

        # Atualizar o ponto x0 para a próxima iteração
        x0 = x1

    # Mostrar mensagem caso o método não encontre a raiz
    print("Não foi possível encontrar uma raiz após todas as iterações.")
    print(table)
    return None

# Definir a variável simbólica
x = sp.symbols('x')

# Função de exemplo
example_function = x**3 - x*9 + 3

# Ponto inicial x0
x0 = 0.5

# Tolerância e número máximo de iterações
tolerance = 10**-4
max_iterations = 20

# Chamada da função para criar a tabela do método de Newton
root_approx_newton = newton_method_table(example_function, x0, tolerance, max_iterations)
