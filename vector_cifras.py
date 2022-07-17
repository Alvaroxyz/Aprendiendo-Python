#función toma un numero y entrega un vector con sus cifras

def cifras(n):
    i=0
    while (10**(i))<=n:
        i=i+1
    k=i-1
    s=n
    digit=[]
    for j in range(k+1):
        d=int(s/(10**(k-j)))
        s=s-(10**(k-j))*d
        digit.extend([d])
    return digit
