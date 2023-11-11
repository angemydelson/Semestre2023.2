import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import HDBSCAN

# https://scikit-learn.org/stable/modules/clustering.html

# Carregue os dados do arquivo CSV
data = pd.read_csv('dados.csv')
# Retira a primeira coluna (nome da pessoa) para realizar o agrupamento
x = data.iloc[:, 1:]

# Crie o modelo usando K-Means e define parâmetros essenciais (número de grupos/clusters)
modelo_ia_1 = KMeans(n_clusters=3)
# Crie o modelo usando HDBScan e define parâmetros essenciais (quantidade mínima de elementos para formar um grupo)
modelo_ia_2 = HDBSCAN(min_cluster_size=2)
# Treina o modelo
modelo_ia_1.fit(x)
modelo_ia_2.fit(x)
# Adicione rótulos aos dados para indicar a qual grupo cada pessoa pertence
data['Grupo KMeans'] = modelo_ia_1.labels_
data['Grupo HDBSCAN'] = modelo_ia_2.labels_
# Ordena dados usando coluna de agrupamento
data = data.sort_values(by=['Grupo KMeans'])
# Salva os resultados em arquivo
data.to_csv('resultado.csv', index=False)
print(data)

# Crie um DataFrame com os centros dos grupos
centros = pd.DataFrame(modelo_ia_1.cluster_centers_, columns=data.columns.values[1:-2])
# Arredonda valores com 2 casas decimais
centros = centros.round(2)
# Adicione uma coluna para identificar os centros dos grupos
centros['Nome'] = ['Centro ' + str(i) for i in range(modelo_ia_1.n_clusters)]
# Salva os resultados em arquivo
centros.to_csv('grupos.csv', index=False)
print(centros)
