#pide un numero y lo entrega invertido

n=int(input('Ingrese un numero: '))


i=0
while 10**(i)<=n:
    i=i+1

k=i-1

lista=[]
s=n
for j in range(k+1):
    d=int(s/(10**(k-j)))
    s=s-(10**(k-j))*d
    lista=[d]+lista

print(lista)