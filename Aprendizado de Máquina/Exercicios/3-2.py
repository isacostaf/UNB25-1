import numpy as np			 
import matplotlib.pyplot as plt 						
from sklearn.linear_model import LinearRegression 

# Independentes
x = np.linspace(10, 28, 10).reshape(-1,1)

# Dependentes
y = np.linspace(100,280,10)

# Criando modelo
modelo = LinearRegression()

# Treinando
modelo.fit(x,y)

# Prevendo
y_reta = modelo.predict(x)

# Grafico
plt.scatter(x,y, color="blue")
plt.plot(x,y_reta,color="black")
plt.title("esse eh o titulo!")
plt.xlabel("temperatura")
plt.ylabel("bicis")
plt.show()