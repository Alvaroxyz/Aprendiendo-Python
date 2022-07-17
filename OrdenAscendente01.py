#Bucles 

#pedir una cantidad n de números enteros e imprimirlos en orden ascendente

cant=int(input("¿Cuántos números va a escribir?"))

lista=[]

i=0

#pido los numeros por pantalla
while i<cant:
    print("Ingrese el ", i, "-ésimo numero")
    numero=int(input())
    lista.extend([numero])
    i=i+1

for j in range(cant-1):#es necesario hacer doble for para que no solo ubique el mayor en el ultimo lugar
    for i in range(cant-j-1):
        if lista[i+1]<lista[i]:
            aux=lista[i+1]
            lista[i+1]=lista[i]
            lista[i]=aux

print(lista)








