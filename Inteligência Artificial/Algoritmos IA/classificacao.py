import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.inspection import DecisionBoundaryDisplay

# Fixar semente aleatória para poder reproduzir os mesmos resultados
semente = 1
np.random.seed(semente)
# Configurar impressão de np.array
np.set_printoptions(precision=2, suppress=True)
# Número de amostras/exemplos/tamanho do conjunto de dados
amostras = 200


# Separar conjunto de dados em conjunto de treinamento e testes
def dividir_dados(dados: np.array, teste: float = .30) -> tuple:
    treinamento = 1 - teste
    # Embaralhar dados
    np.random.shuffle(dados)
    dados_treinamento = dados[0:int(treinamento*amostras), :]
    aux = len(dados_treinamento)
    dados_testes = dados[aux:aux+int(teste*amostras), :]
    return dados_treinamento, dados_testes


# Gerar dados a serem modelados
def gerar_dados(media: tuple, covariancia: tuple) -> np.array:
    # Inicializa matriz (x, y, classe)
    classes = np.empty((1, 3))
    for c in range(len(media)):
        # Gera distribuição
        aux = np.random.multivariate_normal(media[c], covariancia[c], size=amostras)
        # Adiciona coluna para classe
        aux = np.append(aux, np.zeros((amostras, 1)) + c, axis=1)
        # Adiciona no conjunto de dados
        classes = np.append(classes, aux, axis=0)
    # Apaga primeira linah criada na inicialização
    classes = np.delete(classes, 0, 0)
    return classes


def main():
    # Quantidade de classes
    n_classes = 3
    # Coeficientes dos dados gerados (segundo uma distribuição normal multivariada)
    # Passar os dados em tuplas cujo tamanho deverá ser igual à quantidade de classes distintas
    media = ([2, 2], [4, 4], [7, 2])
    covariancia = ([[2, 1], [1, 2]], [[2, -1], [-1, 1]], [[1, 0], [0, 1]])
    dados = gerar_dados(media, covariancia)

    dados_treinamento, dados_testes = dividir_dados(dados, .30)

    # Inicilizar modelo
    # Documentação https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    # solver é a técnica utilizada para o ajuste dos pesos (SGD = stochastic gradient descent)
    # learning_rate_init é o valor inicial da taxa de aprendizado e learning_rate define a estratégia de uso da taxa de aprendizagem
    # max_iter é a quantidade de iterações máximo no treinamento (pode terminar antes usando conjunto de validação)
    # hidden_layer_sizes define a estrutura da rede (quantidade de neurônios em cada camada oculta)
    modelo = MLPClassifier(max_iter=2000, hidden_layer_sizes=())

    # Dois atributos de entrada (bidimensional)
    X = dados_treinamento[:, 0:2]
    # Saída desejada (classes)
    y = dados_treinamento[:, 2]

    # Treinar o modelo
    modelo.fit(X, y)
    acuracia_treinamento = modelo.score(X, y)
    acuracia_testes = modelo.score(dados_testes[:, 0:2], dados_testes[:, 2])
    print("MLP")
    print("Acurácia média no treino:", acuracia_treinamento)
    print("Acurácia média no teste: ", acuracia_testes)

    df_dados = pd.DataFrame(dados, columns=['x', 'y', 'classe'])
    grafico = DecisionBoundaryDisplay.from_estimator(modelo, X, alpha=0.2)
    grafico.ax_.scatter(df_dados['x'], df_dados['y'], c=df_dados['classe'])

    # Configurar tamanho da figura (gráficos)
    plt.figure(figsize=(5, 5))
    plt.title("Classificação")
    plt.scatter(df_dados.loc[df_dados['classe'] == 0]['x'], df_dados.loc[df_dados['classe'] == 0]['y'], label="Classe 0")
    plt.scatter(df_dados.loc[df_dados['classe'] == 1]['x'], df_dados.loc[df_dados['classe'] == 1]['y'], label="Classe 1")
    plt.scatter(df_dados.loc[df_dados['classe'] == 2]['x'], df_dados.loc[df_dados['classe'] == 2]['y'], label="Classe 2")

    plt.legend(loc="lower right")

    plt.show()


main()
