#pide varios números y entrega la suma de sus cifras

#primero creamos una función que haga el proceso de sumar cifras
#tenemos que cargarla del modulo vector_cifras que es donde la tengo

import vector_cifras 

def sumacifras(n):
    c=vector_cifras.cifras(n)
    s=0
    for i in c:
        s=s+i
    return s

#===============================================================

n=int(input('Cuántos números quiere ingresar?: '))

lista=[]
i=1

while i<=n:
    d=int(input(f'Ingrese el numero {i}: '))
    lista=lista+[d]
    i=i+1

for k in lista:
    f=sumacifras(k)
    print(f'{k} -> {f}')



