import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def newton_method_table(f, x0, tol, max_iter, pdf_filename=None):
    # Definir a variável simbólica
    x = sp.symbols('x')

    # Calcular a derivada da função
    f_prime = sp.diff(f, x)

    # Converter a expressão para uma função lambda
    f_lambda = sp.lambdify(x, f, modules=['numpy'])
    f_prime_lambda = sp.lambdify(x, f_prime, modules=['numpy'])

    # Inicializar listas para armazenar dados da tabela
    iteration_list = []
    x_list = []
    f_x_list = []
    f_prime_x_list = []
    x_minus_fx_over_fprime_x_list = []
    interval_size_list = []

    # Loop para executar o método de Newton
    for i in range(max_iter):
        # Calcular os valores da função e de sua derivada no ponto x
        f_x = f_lambda(x0)
        f_prime_x = f_prime_lambda(x0)

        # Calcular o próximo ponto x usando a fórmula do método de Newton
        x1 = x0 - f_x / f_prime_x

        # Calcular o tamanho do intervalo
        interval_size = abs(x1 - x0)

        # Adicionar os valores às listas
        iteration_list.append(i + 1)
        x_list.append(round(x0, 6))
        f_x_list.append(round(f_x, 6))
        f_prime_x_list.append(round(f_prime_x, 6))
        x_minus_fx_over_fprime_x_list.append(round(x1, 6))
        interval_size_list.append(round(interval_size, 6))

        # Verificar se a raiz foi encontrada com a tolerância especificada
        if abs(f_x) < tol:
            print("Raiz aproximada encontrada!")
            print_table(iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list)

            # Salvar a tabela em um arquivo PDF
            if pdf_filename:
                save_table_as_pdf(iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list, pdf_filename)

            return x0

        # Atualizar o ponto x0 para a próxima iteração
        x0 = x1

    # Mostrar mensagem caso o método não encontre a raiz
    print("Não foi possível encontrar uma raiz após todas as iterações.")
    print_table(iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list)

    # Salvar a tabela em um arquivo PDF
    if pdf_filename:
        save_table_as_pdf(iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list, pdf_filename)

    return None

def print_table(iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list):
    # Imprimir a tabela no console
    print("{:<10} {:<10} {:<15} {:<15} {:<25} {:<20}".format(
        "Iteração", "x", "f(x)", "f'(x)", "x - f(x)/f'(x)", "Tamanho do Intervalo"))
    
    for i in range(len(iteration_list)):
        print("{:<10} {:<10} {:<15} {:<15} {:<25} {:<20}".format(
            iteration_list[i], x_list[i], f_x_list[i], f_prime_x_list[i], x_minus_fx_over_fprime_x_list[i], interval_size_list[i]))

def save_table_as_pdf(iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list, pdf_filename):
    # Salvar a tabela em um arquivo PDF usando matplotlib
    with PdfPages(pdf_filename) as pdf:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('tight')
        ax.axis('off')
        table_data = [iteration_list, x_list, f_x_list, f_prime_x_list, x_minus_fx_over_fprime_x_list, interval_size_list]
        table_headers = ["Iteração", "x", "f(x)", "f'(x)", "x - f(x)/f'(x)", "Tamanho do Intervalo"]
        ax.table(cellText=list(zip(*table_data)), colLabels=table_headers, loc='center', cellLoc='center', colColours=['#f3f3f3']*6)
        pdf.savefig(fig, bbox_inches='tight')

# Definir a variável simbólica
x = sp.symbols('x')

# Função de exemplo
example_function = x**3 - x*9 + 3

# Ponto inicial x0
x0 = 0.5

# Tolerância e número máximo de iterações
tolerance = 10**-4
max_iterations = 20

# Nome do arquivo PDF para salvar a tabela
pdf_filename = "resultado_newton.pdf"

# Chamada da função para criar a tabela do método de Newton e salvar em PDF
root_approx_newton = newton_method_table(example_function, x0, tolerance, max_iterations, pdf_filename)
