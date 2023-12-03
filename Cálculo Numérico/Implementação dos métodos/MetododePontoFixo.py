import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def fixed_point_iteration_table(g, x0, tol, max_iter, pdf_filename=None):
    # Definir a variável simbólica
    x = sp.symbols('x')

    # Converter a expressão para uma função lambda
    g_lambda = sp.lambdify(x, g, modules=['numpy'])

    # Inicializar listas para armazenar dados da tabela
    iteration_list = []
    x0_list = []
    x1_list = []
    g_x0_list = []
    interval_size_list = []

    # Loop para executar o método do ponto fixo
    for i in range(max_iter):
        # Calcular o valor da função g no ponto x0
        g_x0 = g_lambda(x0)

        # Calcular o próximo ponto x1 usando a função g
        x1 = g_x0

        # Calcular o tamanho do intervalo
        interval_size = abs(x1 - x0)

        # Adicionar os valores às listas
        iteration_list.append(i + 1)
        x0_list.append(round(x0, 6))
        x1_list.append(round(x1, 6))
        g_x0_list.append(round(g_x0, 6))
        interval_size_list.append(round(interval_size, 6))

        # Verificar se o ponto fixo foi encontrado com a tolerância especificada
        if abs(g_x0 - x0) < tol:
            print("Ponto fixo encontrado!")
            print_table_fixed_point(iteration_list, x0_list, x1_list, g_x0_list, interval_size_list)

            # Salvar a tabela em um arquivo PDF
            if pdf_filename:
                save_table_as_pdf_fixed_point(iteration_list, x0_list, x1_list, g_x0_list, interval_size_list, pdf_filename)

            return x1

        # Atualizar o ponto x0 para a próxima iteração
        x0 = x1

    # Mostrar mensagem caso o método não encontre o ponto fixo
    print("Não foi possível encontrar um ponto fixo após todas as iterações.")
    print_table_fixed_point(iteration_list, x0_list, x1_list, g_x0_list, interval_size_list)

    # Salvar a tabela em um arquivo PDF
    if pdf_filename:
        save_table_as_pdf_fixed_point(iteration_list, x0_list, x1_list, g_x0_list, interval_size_list, pdf_filename)

    return None

def print_table_fixed_point(iteration_list, x0_list, x1_list, g_x0_list, interval_size_list):
    # Imprimir a tabela no console
    print("{:<10} {:<10} {:<10} {:<15} {:<20}".format(
        "Iteração", "x0", "x1", "g(x0)", "Tamanho do Intervalo"))
    
    for i in range(len(iteration_list)):
        print("{:<10} {:<10} {:<10} {:<15} {:<20}".format(
            iteration_list[i], x0_list[i], x1_list[i], g_x0_list[i], interval_size_list[i]))

def save_table_as_pdf_fixed_point(iteration_list, x0_list, x1_list, g_x0_list, interval_size_list, pdf_filename):
    # Salvar a tabela em um arquivo PDF usando matplotlib
    with PdfPages(pdf_filename) as pdf:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('tight')
        ax.axis('off')
        table_data = [iteration_list, x0_list, x1_list, g_x0_list, interval_size_list]
        table_headers = ["Iteração", "x0", "x1", "g(x0)", "Tamanho do Intervalo"]
        ax.table(cellText=list(zip(*table_data)), colLabels=table_headers, loc='center', cellLoc='center', colColours=['#f3f3f3']*5)
        pdf.savefig(fig, bbox_inches='tight')

# Definir a variável simbólica
x = sp.symbols('x')

# Função de exemplo para o método do ponto fixo (use uma função g(x) adequada)
example_function_fixed_point = x**3 - x*9 + 3

# Ponto inicial x0
x0_fixed_point = 0.5

# Tolerância e número máximo de iterações
tolerance_fixed_point = 5*10**-4
max_iterations_fixed_point = 20

# Nome do arquivo PDF para salvar a tabela
pdf_filename_fixed_point = "resultado_ponto_fixo.pdf"

# Chamada da função para criar a tabela do método do ponto fixo e salvar em PDF
root_approx_fixed_point = fixed_point_iteration_table(example_function_fixed_point, x0_fixed_point, tolerance_fixed_point, max_iterations_fixed_point, pdf_filename_fixed_point)
