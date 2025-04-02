# Regressão Linear - Código

```py
import numpy as np # com calculos de matematica e arrays			 
import matplotlib.pyplot as plt # gera gráficos
																
from sklearn.linear_model import LinearRegression # função LinearRegression - pode ser baixada, não precisamos criar

# Dados de exemplo - Cria Arrays
# Horas de estudo (variável independente)
# Reshape para transformar em coluna - Matriz
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)

# Notas obtidas (variável dependente)
y = np.array([2, 4, 5, 7, 10, 11, 14, 17, 20])

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo - Calcula b1 e b0
modelo.fit(X, y)

# Fazendo previsões usando o modelo treinado
# Guarda na variavel os valores de y da reta
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

```np.array```forma um array ([*array*])

```reshape(-1, 1)``` transforma o X em uma coluna

O LinearRegression só trabalho com matrizes pois é assim que o Machine Learning trabalha, por isso, transformamos X em uma coluna, o Y nao precisa ser transformado pois o porgrama entende que eh um vetor relacionado a X, entao ele so encaixa os Y na tabela ja criada por x em seus respectiovs espacos

**Outra Opção:**
```X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).T```


## 📌 Fazendo Previsões
```
y_pred = modelo.predict(X)
```

```modelo.predict(X)``: Realiza a formula da reta com o valor de cada X, ele já tem os melhores valores de b1 e b0 pois ja os descobriu em *modelo.fit(X, y)*
```y_pred```: salvamos aqui o valor de cada Y para cada X da reta que passa no meio dos pontos azuis


