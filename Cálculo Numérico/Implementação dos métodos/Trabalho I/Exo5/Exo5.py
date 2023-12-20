import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd

def finite_difference_method(h):
    x = np.arange(0, 1 + h, h)
    n = len(x)

    A = np.zeros((n, n))
    b = np.zeros(n)

    # Construir a matriz tridiagonal e o vetor do lado direito
    for i in range(1, n - 1):
        A[i, i - 1] = 1 / (h**2) - x[i] / (2 * h)
        A[i, i] = -2 / (h**2) + 1
        A[i, i + 1] = 1 / (h**2) + x[i] / (2 * h)
        b[i] = x[i] - x[i] * x[i] - np.exp(x[i]) * (x[i]**2 + 1)

    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    b[0] = 0
    b[n - 1] = np.exp(1)

    # Resolver o sistema linear
    y = solve(A, b)

    return x, y

def plot_solution(x, y, label):
    plt.plot(x, y, label=label)

def save_to_pdf_and_table(x, y, filename):
    plt.figure(figsize=(8, 6))
    plt.title("Finite Difference Method")
    plt.xlabel("x")
    plt.ylabel("y")
    
    plot_solution(x, y, "h = 0.1")

    # Repetir para h = 0.05
    x_05, y_05 = finite_difference_method(0.05)
    plot_solution(x_05, y_05, "h = 0.05")

    # Repetir para h = 0.01
    x_01, y_01 = finite_difference_method(0.01)
    plot_solution(x_01, y_01, "h = 0.01")

    plt.legend()
    plt.grid(True)

    plt.savefig(filename.replace('.pdf', '_plot.pdf'))

    # Criar e salvar a tabela em PDF
    data = {"x": x, "h=0.1": y, "h=0.05": y_05[:len(x)], "h=0.01": y_01[:len(x)]}
    df = pd.DataFrame(data)

    table_filename = filename.replace('.pdf', '_table.pdf')
    save_table_to_pdf(df, table_filename)

    plt.show()

def save_table_to_pdf(df, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    doc.build([table])

# Executar para h = 0.1 e salvar em "finite_difference_solution.pdf"
x, y = finite_difference_method(0.1)
save_to_pdf_and_table(x, y, "finite_difference_solution.pdf")
