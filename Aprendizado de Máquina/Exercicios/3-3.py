import numpy as np			 
import matplotlib.pyplot as plt 						
from sklearn.linear_model import LinearRegression 

# Independentes
x1 = np.array([3,2,4,5,3,4,5,6,4,3]).reshape(-1,1)
x2 = np.array([5,3,6,2,4,5,3,2,4,6]).reshape(-1,1)


# Juntando
x = np.hstack((x1, x2))  

# Dependente:
y = np.array([200,150,250,300,225,275,350,400,275,225])

# Criando modelo:
modelo = LinearRegression()

# Treinando
modelo.fit(x,y)

# Prevendo
y_reta = modelo.predict(x)

# Grafico
plt.scatter(x1,y, color="purple")
plt.plot(x1,y_reta,color="black")
plt.show()