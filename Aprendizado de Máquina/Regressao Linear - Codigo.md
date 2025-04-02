# Regressão Linear - Código

```py
import numpy as np # importa a biblioteca NumPy que trabalha com 
									 # calculos de matematica e arrays
									 
import matplotlib.pyplot as plt # importa o MatPlotLib 
																# que gera gráficos
																
from sklearn.linear_model import LinearRegression # importa a função
																									# LinearRegression da biblioteca
																									# sklearn, ela pode ser baixada
																									# não precisamos criar

# Dados de exemplo
# Horas de estudo (variável independente)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)

# Notas obtidas (variável dependente)
y = np.array([2, 4, 5, 7, 10, 11, 14, 17, 20])

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo com os dados
modelo.fit(X, y)

# Fazendo previsões usando o modelo treinado
y_pred = modelo.predict(X)

# Plotando os dados originais e a linha de regressão
plt.scatter(X, y, color='blue')  # Pontos originais
plt.plot(X, y_pred, color='red')  # Linha de regressão
plt.title("Relação entre Horas de Estudo e Notas")
plt.xlabel("Horas de Estudo")
plt.ylabel("Notas")
plt.show()
fjnksjfhkfsik

```