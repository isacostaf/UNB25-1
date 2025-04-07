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
