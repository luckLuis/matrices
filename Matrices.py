#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np


fila1 = int(input("Número de filas de la matriz 1: "))
columna1 = int(input("Número de columnas de la matriz 1: "))

fila2 = int(input("Número de filas de la matriz 2: "))
columna2 = int(input("Número de columnas de la matriz 2: "))

if fila1 != fila2 or columna1 != columna2:
    print("No se puede realizar la operación!")
    
else:
    matriz1 = np.zeros((fila1, columna1))
    matriz2 = np.zeros((fila2, columna2))

    print("Introduce los elementos de la matriz 1: ")
    for i in range(fila1):
        for j in range (columna1):
            matriz1[i, j] = input("Numero A[" + str(i+1) + "," + str(j+1) + "]: ")

    print("Introduce los elementos de la matriz 2: ")
    for i in range(0,fila2):
        for j in range (0,columna2):
            matriz2[i, j] = input("Numero B[" + str(i+1) +  "," + str(j+1) + "]: ") 
                
    aux = np.dot(matriz1, matriz2)
     
    print("===============================================")   
    print(matriz1)
    
    print("===============================================") 
    
    print(matriz2)
    
    print("===============================================")  

    print(aux)


# In[ ]:


5
6


# In[ ]:





# In[ ]:





# In[ ]:




