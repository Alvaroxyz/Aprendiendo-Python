#A Ana le gusta jugar con numeros y hacer secuencias de ellos. Ahora esta jugando a hacer secuencias
#de la siguiente forma: primero escoge un entero positivo m, que sera el primer termino de la secuencia,
#a1 = m. Despues, para todo i>=2, ai es el menor multiplo de i que es mayor o igual que a_{i-1}. 
#Estos valores de m para los que la secuencia resultante no tiene dos numeros
#consecutivos iguales se llaman numeros especiales.
#Puedes ayudar a Ana a encontrar el n-esimo numero especial?

import numpy as np 

m = 9
tope = 1000

def secuencia_siguientes_multiplos_2(m):
    """
    Retorna 1 si el numero es especial y 0 si no lo es. Contando su sucesión hasta el tope.
    """
    bandera = 1
    valor_anterior_anterior = m
    valor_anterior = m
    termino_siguiente = 2
    while termino_siguiente<tope:
        if valor_anterior%termino_siguiente == 0:
            bandera = 0
            break
        elif 3<=termino_siguiente and termino_siguiente - valor_anterior == valor_anterior - valor_anterior_anterior:
            break
        else:
            valor_anterior_anterior = valor_anterior
            valor_anterior = (np.floor(valor_anterior/termino_siguiente)+1)*termino_siguiente
        termino_siguiente += 1
    return bandera


def numero_especial_n(n):
    evalua_especial = 1
    cantidad_especiales = 0
    while cantidad_especiales<n:
        if evalua_especial%2 != 0 and secuencia_siguientes_multiplos_2(evalua_especial) == 1:
            cantidad_especiales += 1
        else:
            None
        evalua_especial +=1
    return evalua_especial-1


a = numero_especial_n(3)
print(a)
