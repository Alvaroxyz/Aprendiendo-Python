#secuencias de siguientes múltiplos

#encontrar el n-esimo numero especial

#programa que organiza la secuencia para un numero m

m=int(input('Cual sucesion quiere: '))


sucesor_a=m
i=2


tope=1000

no_especial=0
t=1

while t<=m:
    k=1
    while i*k<=sucesor_a and i<=tope:
        k=k+1
    if sucesor_a==i*k:
        no_especial=no_especial+1
    else:
        sucesor_a=i*k
    i=i+1
    t=t+1



print(f'Cantidad de especiales: {m-no_especial}')








for i in range(2,m+1):
    k=1
    while i*k<=sucesor_a:
        k=k+1

sucesor_a=i*k

