#para toro entero n>1 considere p1,..,pk los primos que lo 
# dividen defina el producto p(n)=(p1-1)...(pk-1)decimos 
# que n es significativo si p(n)y p(n+1) son divisibles 
# entre 42. encontrar todos los numeros significativos menores que 500

#SOLUCIÓN

#Lista con los primos hasta 500

#p=[2]

#for i in range(3,500):
#    s=0
#    for j in range(2,i):
#        if i%j==0:
#            break
#        else:
#            s=s+1
#        if s==i-2:
#            p.append(i) 
#    i=i+1 


p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 
61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 
293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 
389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]


#Función que calcula p(n)

def pn(n):
    pn=1
    for i in p:
        if n%i==0:
            pn=pn*(i-1)
    return(pn)


#Función que evalúa si n es significativo

def sig(n):
    sig=0
    if pn(n)%42==0 and pn(n+1)%42==0:
        sig=1
    return sig 

#encontrando los significativos menores que 500

k=1
lista =[]

while k<500:
    if sig(k)==1:
        lista.append(k)
    k=k+1

print(lista)
    
#SOLUCIÓN: El único significativo es 421.



