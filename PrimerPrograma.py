nombre = "Álvaro"
apellido = "Riaño"
print(nombre, apellido)

#creamos una función que repite dos veces


def print_twice(alvaro):
    print(alvaro)
    print(alvaro)


#vamos a probarla 

print_twice('lolcast ahora si')


#creamos otra función 

def sumados(a,b):
    c=a+b
    print(c)

#la probamos 

sumados(3,4)

#funcinoes sin print pero con return para que retorne los valores

def resta(a,b):
    resultado=a-b
    return resultado

#la corremos, no se muestra en pantalla, pero si hace el cálculo 
resta(100, 67)

#si queremos que la muestre 

print(resta(100,67))


def print_spam(spam):
    print(spam)


print_twice(print_spam('spam'))#esta no funciona porque lo que hace print_spam es enviar una orden de print, no es que retorne
#un valor ni nada aceptable como argumento para print_twice. Entonces lo que pasa es que el programa ejecuta una vez la función
#print_spam por lo que aparece 'spam' una vez en pantalla pero print_twice no puede leerlo, así que sale none y none. 
#lo mismo ocurre con 

print_twice(print_twice('alvaro'))

#RECURSIÓN

#el ejemplo de la cuenta regresiva

def count_down(n):
    if n<=0:
        print('Cuenta regresiva')
    else:
        print(n)
        count_down(n-1)

count_down(10)

#entrada de datos

entrada1=input('ingrese cualqueir vaina: ') #guarda datos de tipo string 

print(f"hola {entrada1}") 

#pedir enteros 

numero1=int(input('Ahora sí escriba un numero pa: '))#analogamente si queremos un float

print(f"Este es el sucesor del número {numero1+1}")



