import numpy as np			 
import matplotlib.pyplot as plt 						
from sklearn.linear_model import LinearRegression 

# Independentes - Hora de estudo
x = np.linspace(1,10,10).reshape(-1,1)

# Dependentes - Notas
y = np.linspace(50, 95, 10)

# Cria Modelo
modelo = LinearRegression()

# Treina
modelo.fit(x,y)

# Previsoes
y_reta = modelo.predict(x)

#Plota
plt.scatter(x,y, color='blue')
plt.plot(x,y_reta, color='red')
plt.title("estudo x notas")
plt.xlabel("horas de estudo")
plt.ylabel("notas")
plt.show()