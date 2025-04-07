# Regressão Minimos Quadrados
## Simplificado:
```
import numpy as np
import matplotlib.pyplot as plt

# Independentes
tempo_de_estudo = np.array([2, 4, 6, 8, 5, 3, 7, 1, 9, 10]).reshape(-1,1)
horas_de_sono = np.array([6, 7, 8, 5, 6, 7, 8, 5, 7, 9]).reshape(-1,1)
videoaulas = np.array([1, 2, 3, 2, 2, 1, 3, 1, 4, 5]).reshape(-1,1)

# Dependente (nota final)
notas = np.array([60, 70, 80, 75, 72, 65, 85, 55, 90, 95])

# Juntando as variáveis independentes
x = np.hstack((tempo_de_estudo, horas_de_sono, videoaulas))

# Cálculo da regressão (mínimos quadrados)
x_b = np.c_[np.ones((10, 1)), x]  # Adiciona coluna de 1s para o intercepto
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(notas)

# Prevendo com os próprios dados
y_reta = x_b.dot(theta_best)

# Gráfico (só tempo de estudo vs nota)
plt.scatter(tempo_de_estudo, notas, color='blue', label='Dados')
plt.plot(tempo_de_estudo, y_reta, color='red', label='Ajuste Linear')
plt.xlabel('Tempo de Estudo (horas)')
plt.ylabel('Nota')
plt.title('Nota em função do tempo de estudo')
plt.legend()
plt.show()

# Previsão para novos alunos
novos_alunos = np.array([
    [5, 7, 2],   # aluno 1
    [9, 6, 4]    # aluno 2
])
novos_alunos_b = np.c_[np.ones((2, 1)), novos_alunos]
notas_previstas = novos_alunos_b.dot(theta_best)

print("Notas previstas:")
print(notas_previstas)
```

# Cálculo da regressão (mínimos quadrados)

```
x_b = np.c_[np.ones((10, 1)), x]  # Adiciona coluna de 1s para o intercepto
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(notas)
````

O intercepto é quanto o Y vale quando todos os x sao zero, ou seja, se o aluno nem estudou, nao dormiu e nao viu video aula ele ainda assim nao tirou zero, tirou uma nota, essa nota eh o intercepto, eh o valor base quando nenhum dos x tem valor

-> no ultimo codigo usavamos o ```LinearRegression()``` que adicionava uma coluna pro intercepto automaticamente, mas aqui precisamos fazer manualmente

```np.ones((10, 1))```: cria uma tabela de 10 linhas e uma coluna todas com o valor 1, na fomula temos o teta(θ) sempre multiplicando x1,x2,x3... mas o primeiro θ nao eh multiplicado por nenhum termo, ou seja eh multiplicado por 1. 

nessa tabela x temos todos os valores que multplicam os tetas, mas nos faltava colocar algo para que o θ0 nao fosse esquecido ou desconsiderado, por isso agregamos uma coluna no comeco sendo 1, pq quando ai fica 1*θ + x1*θ + x2*θ... os tetas ainda vamos descobrir, esss tabela sao apenas dos valores q multiplicam os tetas

**y = 1⋅θ0 ​+ x1​⋅θ1 ​+ x2​⋅θ2 + x3​⋅θ3**

```np.c_[]```: vamos concatenar essa tabela com a tabela do x, ou seja adiconar essa coluna na tabela x, cada linha agr vai ter uma a primeira coluna com o valor de intercepto (1)

chamamos essa nova tabela de **x_b**

```
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(notas)
```

```x_b.T```
Transposta de x_b

```x_b.T.dot(x_b)```
Multiplicamos a transposta de x_b por x_b assim fazemos uma grande matriz quadratica com todas combinações entre variaveis e mostrando como se relacionam entre si

```np.linalg.inv(x_b.T.dot(x_b))```
Calculamos a inversa dessa matriz, isso serve p isolar os θ

```dot(x_b.T)```
multiplica pela trasnposta de novo

```.dot(notas)```
multiplica pela notas que eh o valor que queremos descobrir

📦 Resumão visual da fórmula:
θ = (X.T X)ˆ−1 *X.T y

```
novos_alunos = np.array([
    [5, 7, 2],  # aluno 1
    [9, 6, 4]   # aluno 2
])

novos_alunos_b = np.c_[np.ones((2, 1)), novos_alunos]

notas_previstas = novos_alunos_b.dot(theta_best)
``` 

criamosnovos alunos, cada aluno tem 3 variaveis (hr de estudo, num de ex, presenca) entao por isso as 3 coluna
comecamos adicionando a coluna com 1 pro θ
concatenamos

e fazemos
resultado = tabela_b.dot(theta_best)
