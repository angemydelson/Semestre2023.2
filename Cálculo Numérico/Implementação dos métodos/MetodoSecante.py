import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import math

def secant_method_table(f, x0, x1, tol, max_iter, pdf_filename=None):
    # Definir a variável simbólica
    x = sp.symbols('x')

    # Converter a expressão para uma função lambda
    f_lambda = sp.lambdify(x, f, modules=['numpy'])

    # Inicializar listas para armazenar dados da tabela
    iteration_list = []
    x0_list = []
    x1_list = []
    f_x0_list = []
    f_x1_list = []
    x2_list = []
    interval_size_list = []

    # Loop para executar o método da secante
    for i in range(max_iter):
        # Calcular os valores da função nos pontos x0 e x1
        f_x0 = f_lambda(x0)
        f_x1 = f_lambda(x1)

        # Calcular o próximo ponto x2 usando a fórmula do método da secante
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        # Calcular o tamanho do intervalo
        interval_size = abs(x2 - x1)

        # Adicionar os valores às listas
        iteration_list.append(i + 1)
        x0_list.append(round(x0, 6))
        x1_list.append(round(x1, 6))
        f_x0_list.append(round(f_x0, 6))
        f_x1_list.append(round(f_x1, 6))
        x2_list.append(round(x2, 6))
        interval_size_list.append(round(interval_size, 6))

        # Verificar se a raiz foi encontrada com a tolerância especificada
        if abs(f_x1) < tol:
            print("Raiz aproximada encontrada!")
            print_table_secant(iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list)

            # Salvar a tabela em um arquivo PDF
            if pdf_filename:
                save_table_as_pdf_secant(iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list, pdf_filename)

            return x1

        # Atualizar os pontos x0 e x1 para a próxima iteração
        x0, x1 = x1, x2

    # Mostrar mensagem caso o método não encontre a raiz
    print("Não foi possível encontrar uma raiz após todas as iterações.")
    print_table_secant(iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list)

    # Salvar a tabela em um arquivo PDF
    if pdf_filename:
        save_table_as_pdf_secant(iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list, pdf_filename)

    return None

def print_table_secant(iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list):
    # Imprimir a tabela no console
    print("{:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<20}".format(
        "Iteração", "x0", "x1", "f(x0)", "f(x1)", "x2", "Tamanho do Intervalo"))
    
    for i in range(len(iteration_list)):
        print("{:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<20}".format(
            iteration_list[i], x0_list[i], x1_list[i], f_x0_list[i], f_x1_list[i], x2_list[i], interval_size_list[i]))

def save_table_as_pdf_secant(iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list, pdf_filename):
    # Salvar a tabela em um arquivo PDF usando matplotlib
    with PdfPages(pdf_filename) as pdf:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('tight')
        ax.axis('off')
        table_data = [iteration_list, x0_list, x1_list, f_x0_list, f_x1_list, x2_list, interval_size_list]
        table_headers = ["Iteração", "x0", "x1", "f(x0)", "f(x1)", "x2", "Tamanho do Intervalo"]
        ax.table(cellText=list(zip(*table_data)), colLabels=table_headers, loc='center', cellLoc='center', colColours=['#f3f3f3']*7)
        pdf.savefig(fig, bbox_inches='tight')

# Definir a variável simbólica
x = sp.symbols('x')

# Função de exemplo
example_function_secant =  2*x**2 - x*3 + sp.log(x)


# Pontos iniciais x0 e x1
x0_secant = 1
x1_secant = 2

# Tolerância e número máximo de iterações
tolerance_secant = 10**-4
max_iterations_secant = 20

# Nome do arquivo PDF para salvar a tabela
pdf_filename_secant = "resultado_secante.pdf"

# Chamada da função para criar a tabela do método da secante e salvar em PDF
root_approx_secant = secant_method_table(example_function_secant, x0_secant, x1_secant, tolerance_secant, max_iterations_secant, pdf_filename_secant)
