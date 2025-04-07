import numpy as np			 
import matplotlib.pyplot as plt 						
from sklearn.linear_model import LinearRegression 

# Independentes
x1 = np.array([120,150,80,200,100,130,160,110,180,140]).reshape(-1,1)
x2 = np.array([3,4,2,5,3,3,4,3,4,3]).reshape(-1,1)
x3 = np.array([5,7,10,3,15,4,6,8,2,12]).reshape(-1,1)

# Dependentes
y = np.array([300,350,200,500,250,320,360,280,480,310])

# juntando
x = np.hstack((x1,x2,x3))

# criando modelo
modelo = LinearRegression()

# treinando
modelo.fit(x,y)

# prevendo
y_reta = modelo.predict(x)

# grafico
plt.scatter(x1,y, color="blue")
plt.plot(x1,y_reta, color="red")
plt.show()