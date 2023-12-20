import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Especificando o número de linhas a serem lidas
num_linhas = 50 

# Lendo o arquivo CSV
nome_arquivo = 'life.csv'  
dados = pd.read_csv(nome_arquivo, nrows=num_linhas)

""" for i in range(len(dados['GDP'])):
    dados.loc[i, 'GDP'] = dados.loc[i, 'GDP'] """

Y = dados['GDP']
X = dados['Life_expectancy']

# Polynomial Regression
degree = 3 
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X.values.reshape(-1, 1))

poly_model = LinearRegression()
poly_model.fit(X_poly, Y)

X_range = np.linspace(min(X), max(X), 1000).reshape(-1, 1)
X_range_poly = poly_features.transform(X_range)
y_poly_pred = poly_model.predict(X_range_poly)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X.values.reshape(-1, 1), Y)
y_linear_pred = linear_model.predict(X_range)

# Exponential Regression
def exponential_function(x, a, b, c):
    return a * np.exp(b * x) + c

#Chutes iniciais (exponencial)
max_Y = np.max(Y)
min_Y = np.min(Y)
initial_guess_exp = [max_Y, 0.001, min_Y]

params_exp, covariance_exp = curve_fit(exponential_function, X, Y, p0=initial_guess_exp, maxfev=10000)
y_exp_pred = exponential_function(X_range, *params_exp)

#Valores de R²
r2_poly = r2_score(Y, poly_model.predict(X_poly))
r2_linear = r2_score(Y, linear_model.predict(X.values.reshape(-1, 1)))
r2_exp = r2_score(Y, exponential_function(X, *params_exp))

# Printando matrizes principais
print("Polynomial Regression Coefficients:")
print(poly_model.coef_)
print("\nLinear Regression Coefficients:")
print(linear_model.coef_)
print("\nExponential Regression Parameters:")
print(params_exp)
print("\nPolynomial Features Matrix:")
print(X_poly)
print("\nOriginal Features Matrix:")
print(X.values.reshape(-1, 1))

# Plotting
plt.scatter(X, Y, label='Original data')
plt.plot(X_range, y_poly_pred, color='red', label=f'Polynomial Regression (degree={degree}), R2={r2_poly:.2f}')
plt.plot(X_range, y_linear_pred, color='blue', label=f'Linear Regression, R2={r2_linear:.2f}')
plt.plot(X_range, y_exp_pred, color='green', label=f'Exponential Regression, R2={r2_exp:.2f}')
plt.legend()
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Polynomial, Linear, and Exponential Regression')
plt.show()

print(f'R-squared (Polynomial): {r2_poly:.2f}')
print(f'R-squared (Linear): {r2_linear:.2f}')
print(f'R-squared (Exponential): {r2_exp:.2f}')
