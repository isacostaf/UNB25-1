# Regressão Linear - Código

```py
import numpy as np # com calculos de matematica e arrays			 
import matplotlib.pyplot as plt # gera gráficos
																
from sklearn.linear_model import LinearRegression # ifunção LinearRegression - pode ser baixada, não precisamos criar

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

```

## 📌 Importação de bibliotecas
```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
````


```import numpy as np:``` Importa o NumPy, que é uma biblioteca para trabalhar com arrays e fazer cálculos matemáticos.

```import matplotlib.pyplot as plt:``` Importa o Matplotlib, usado para criar gráficos.

```from sklearn.linear_model import LinearRegression:``` Importa a função LinearRegression da biblioteca sklearn, que é usada para criar o modelo de regressão linear.


## 📌 Criando os dados
```
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([2, 4, 5, 7, 10, 11, 14, 17, 20])
```
Estamos declarando os valores de X e depois os de Y equivalentes a cada valor de X

```np.array```forma um array ([*array*])

```reshape(-1, 1)```
transforma o vetor X em uma coluna 2D
O ```LinearRegression```trabalha com tabelas e não com vetores por isso precisamos usar o ```reshape(-1, 1)``` em X, para transformar ele em uma coluna
não precisamos usar o reshape em Y porque ja formamos a tabela em X, o programa entende e simplesmente encaixa os valores de y em seus consecutivos lugares de X na tabela que ja foi montada em X

Tambem podemos usar:
```.T```
```X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]]).T```
