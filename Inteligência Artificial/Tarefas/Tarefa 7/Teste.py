import pandas as pd
from sklearn.cluster import KMeans

# Carregue os dados do arquivo CSV
data = pd.read_csv('resultado.csv')

# Retira a primeira coluna (nome da pessoa) para realizar o agrupamento
x = data.iloc[:, 1:]

# Crie o modelo usando K-Means e define o número de clusters
modelo_ia_1 = KMeans(n_clusters=3)

# Treina o modelo
modelo_ia_1.fit(x)

# Adicione rótulos aos dados para indicar a qual grupo cada pessoa pertence
data['Grupo KMeans'] = modelo_ia_1.labels_

# Calcular as estatísticas para cada cluster
cluster_stats = data.groupby('Grupo KMeans').describe()

# Salvar as estatísticas em um arquivo
cluster_stats.to_csv('cluster_stats.csv')

# Imprimir as estatísticas
print(cluster_stats)
