import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

# Fixar semente aleatória para poder reproduzir os mesmos resultados
semente = 1
np.random.seed(semente)
# Configurar impressão de np.array
np.set_printoptions(precision=2, suppress=True)
# Número de amostras/exemplos/tamanho do conjunto de dados
amostras = 100


# Separar conjunto de dados em conjunto de treinamento, testes e validação
def dividir_dados(dados: np.array, teste: float = .15, validacao: float = .15) -> tuple:
    treinamento = 1 - teste - validacao
    # Embaralhar dados
    np.random.shuffle(dados)
    dados_treinamento = dados[0:int(treinamento*amostras), :]
    aux = len(dados_treinamento)
    dados_testes = dados[aux:aux+int(teste*amostras), :]
    aux += len(dados_testes)
    dados_validacao = dados[aux:, :]
    return dados_treinamento, dados_testes, dados_validacao


# Função de erro (MSE — Mean Squared Error)
def erro_quadratico_medio(y_previsto: np.array, y: np.array) -> float:
    return (1/y.size) * np.sum((y - y_previsto)**2)


def erro_modelo(dados: np.array, modelo: tuple) -> float:
    x = dados[:, 0]
    y = dados[:, 1]
    y_previsto = previsao_modelo(x, modelo)
    return erro_quadratico_medio(y_previsto, y)


def previsao_modelo(x: np.array, modelo: tuple) -> float:
    b = modelo[0]
    w1 = modelo[1]
    w2 = 0
    if len(modelo) > 2:
        w2 = modelo[2]
    y_previsto = w2 * x ** 2 + w1 * x + b
    return y_previsto


# Gerar dados a serem modelados
def gerar_dados(intervalo_x: tuple, coeficientes: tuple, ruido: int) -> np.array:
    x = np.random.randint(intervalo_x[0], intervalo_x[1], size=amostras)
    ruido_gerado = np.random.uniform(-ruido, ruido, size=amostras)
    y = coeficientes[1] * x + coeficientes[0] + ruido_gerado
    if len(coeficientes) > 2:
        y += coeficientes[2] * x**2
    if len(coeficientes) > 3:
        y += coeficientes[3] * x**3
    return np.vstack([x, y]).T


def regressao_linear(dados: np.array) -> tuple:
    x = dados[:, 0]
    y = dados[:, 1]
    # Inicializar pesos
    b = np.zeros(1)
    w = np.random.rand(1)
    # parâmetros do treinamento
    # alfa — taxa de aprendizado (controla a velocidade no ajuste dos pesos)
    alfa = 0.1
    num_epocas = 20
    # executa treinamento
    for epoca in range(num_epocas):
        y_previsto = previsao_modelo(x, (b, w))
        #erro = erro_quadratico_medio(y_previsto, y)
        #print("Erro:", erro)
        db, dw = gradiente_modelo_linear(y_previsto, y, x)
        # atualizar pesos (aprendizado)
        # como desejamos minimizar o erro, devemos ir no sentido contrário indicado pelo gradiente
        b += alfa * -db
        w += alfa * -dw
    return b, w


def regressao_polinomial_quadratica(dados: np.array) -> tuple:
    x = dados[:, 0]
    y = dados[:, 1]
    # Inicializar pesos
    b = np.zeros(1)
    w1 = np.random.rand(1)
    w2 = np.random.rand(1)
    # parâmetros do treinamento
    # alfa — taxa de aprendizado (controla a velocidade no ajuste dos pesos)
    alfa = 0.05
    num_epocas = 200
    # executa treinamento
    for epoca in range(num_epocas):
        y_previsto = previsao_modelo(x, (b, w1, w2))
        #erro = erro_quadratico_medio(y_previsto, y)
        #print("Erro:", erro)
        db, dw1, dw2 = gradiente_modelo_quadratico(y_previsto, y, x)
        # atualizar pesos (aprendizado)
        # como desejamos minimizar o erro, devemos ir no sentido contrário indicado pelo gradiente
        b += alfa * -db
        w1 += alfa * -dw1
        w2 += alfa * -dw2
    return b, w1, w2


def mlp(dados: np.array):
    modelo = MLPRegressor(max_iter=500, hidden_layer_sizes=(100, 100, 100))
    x = dados[:, 0:1]
    y = dados[:, 1]

    modelo.fit(x, y)
    return modelo


# Computar a derivada da função de erro em relação aos pesos do modelo (indica sentido para maximizar a função)
def gradiente_modelo_linear(y_previsto: np.array, y: np.array, x: np.array) -> tuple:
    db = (-2 / y.size) * np.sum(y - y_previsto) * 1
    dw = (-2 / y.size) * np.sum((y - y_previsto) * x)
    return db, dw


# Computar a derivada da função de erro em relação aos pesos do modelo (indica sentido para maximizar a função)
def gradiente_modelo_quadratico(y_previsto: np.array, y: np.array, x: np.array) -> tuple:
    db = (-2 / y.size) * np.sum(y - y_previsto) * 1
    dw1 = (-2 / y.size) * np.sum((y - y_previsto) * x)
    dw2 = (-2 / y.size) * np.sum((y - y_previsto) * x**2)
    return db, dw1, dw2


def main():
    # Coeficientes dos dados gerados
    # (b, a) - ax + b - função linear ou
    # (c, b, a) - ax^2 + bx + c - função quadrática
    # (d, c, b, a) - ax^3 + bx^2 + cx + d - função de terceiro grau
    coeficientes = (12, 7, -8, -1)
    # Intervalo de valores para x
    intervalo = (-100, 100)
    # Erro amostral para mais ou para menos em y
    erro_amostral = 10
    dados = gerar_dados(intervalo, coeficientes, erro_amostral)

    dados_treinamento, dados_testes, dados_validacao = dividir_dados(dados, .15, 0)
    # Padronizar os dados com média = 0 e desvio padrão = 1
    # A padronização (normalização z) aumenta a eficiência do treinamento e evita problemas numéricos ocasionados pro valores muito grandes
    media = np.mean(dados, axis=0)
    desvio_padrao = np.std(dados, axis=0)
    dados_padrao = (dados - media) / desvio_padrao
    dados_treinamento_padrao = (dados_treinamento - media) / desvio_padrao
    dados_testes_padrao = (dados_testes - media) / desvio_padrao
    dados_validacao_padrao = (dados_validacao - media) / desvio_padrao

    # Regressão Linear
    modelo_linear = regressao_linear(dados_treinamento_padrao)

    # Regressão Quatrática
    modelo_quadratico = regressao_polinomial_quadratica(dados_treinamento_padrao)

    # Regressão MLP
    modelo_mlp = mlp(dados_treinamento_padrao)

    erro_treinamento = erro_modelo(dados_treinamento_padrao, modelo_linear)
    erro_testes = erro_modelo(dados_testes_padrao, modelo_linear)
    print("Modelo Linear")
    print("Erro treino:", erro_treinamento)
    print("Erro teste: ", erro_testes)

    erro_treinamento = erro_modelo(dados_treinamento_padrao, modelo_quadratico)
    erro_testes = erro_modelo(dados_testes_padrao, modelo_quadratico)
    print("Modelo Quadrático")
    print("Erro treino:", erro_treinamento)
    print("Erro teste: ", erro_testes)

    erro_treinamento = erro_quadratico_medio(modelo_mlp.predict(dados_treinamento_padrao[:, 0:1]), dados_treinamento_padrao[:, 1])
    erro_testes = erro_quadratico_medio(modelo_mlp.predict(dados_testes_padrao[:, 0:1]), dados_testes_padrao[:, 1])
    print("Modelo MLP")
    print("Erro treino:", erro_treinamento)
    print("Erro teste: ", erro_testes)

    # Configurar tamanho da figura (gráficos)
    plt.figure(figsize=(10, 10))

    df_treinamento = pd.DataFrame(dados_treinamento, columns=['x', 'y'])
    df_testes = pd.DataFrame(dados_testes, columns=['x', 'y'])
    # Multiplicar pelo desvio e somar a média para despadronizar os dados (retornar a escala original)
    df_dados = pd.DataFrame(dados, columns=['x', 'y'])
    df_dados['modelo_linear'] = previsao_modelo(dados_padrao[:, 0], modelo_linear) * desvio_padrao[1] + media[1]
    df_dados['modelo_quadratico'] = previsao_modelo(dados_padrao[:, 0], modelo_quadratico) * desvio_padrao[1] + media[1]
    df_dados['modelo_mlp'] = modelo_mlp.predict(dados_padrao[:, 0:1]) * desvio_padrao[1] + media[1]
    # É necessário ordenar os elementos de acordo com x para o gráfico de linha ser gerado corretamente
    df_dados = df_dados.sort_values(by=['x'])

    plt.title("Regressão")
    plt.scatter(df_treinamento['x'], df_treinamento['y'], label="treinamento")
    plt.scatter(df_testes['x'], df_testes['y'], label='teste')
    plt.plot(df_dados['x'], df_dados['modelo_linear'], color="purple", linewidth=1, linestyle="-", label="modelo linear")
    plt.plot(df_dados['x'], df_dados['modelo_quadratico'], color="red", linewidth=1, linestyle="-.", label="modelo quadrático")
    plt.plot(df_dados['x'], df_dados['modelo_mlp'], color="blue", linewidth=1, linestyle="--",
             label="modelo MLP")
    plt.legend(loc="lower right")

    plt.show()


main()
