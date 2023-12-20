import copy
from math import *

def triangular(entrada):
	saida = [None for x in range(len(entrada))]
	for i in reversed(range(0,len(entrada[0])-1)): #for (int i=sizeof(entrada)/sizeof(entrada[0]); i > 0; i--)
		soma = 0
		for j in reversed(range(i,len(entrada))):
			if i != j: #se não for o elemento pivô
				soma += saida[j]*entrada[i][j] #calcula e coloca tudo na variavel soma pra subtrair depois
			else: # se não for elemento pivô, calcula o x( faz a regressão )
				saida[i]=(entrada[i][len(entrada[0])-1]-soma)/entrada[i][i] #subtrai soma
				break
	return saida

def escalonamento(entrada):
	n = len(entrada) # calculando o n (numero de variaveis e equacoes)
	anterior = copy.deepcopy(entrada) # usando o deepcopy para fazer a cópia do vetor
	proximo = copy.deepcopy(entrada)
	for k in range(1,n): #k iterações de 2 em diante (1, por conta do índice começar com 0)
		if proximo[k][k] == 0: #caso em que o pivô é nulo.
			return None #implementar tratamento (troca de linha)
		anterior = copy.deepcopy(proximo)
		for i in range(n): # percorrendo linhas
			for j in range(n+1): # e as colunas (n+1 por conta do `b` da matriz aumentada)
				if i < k: # aplicando o algoritmo
					proximo[i][j] = anterior[i][j]
				elif i > k-1 and j < k:
					proximo[i][j] = 0
				else:
					proximo[i][j] = anterior[i][j]-(anterior[i][k-1]/anterior[k-1][k-1]*anterior[k-1][j])
	return proximo #pronto, transformou em matriz triangular superior equivalente à matriz aumentada do início

def gauss(entrada):
	return triangular(escalonamento(entrada))

entrada = [[2,0,0,0,3],[1,1.5,0,0,4.5],[0,-3,0.5,0,-6.6],[2,-2,1,1,0.8]]
print(gauss(entrada))