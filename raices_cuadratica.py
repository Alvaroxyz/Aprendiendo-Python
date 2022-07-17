#calcula las raices de una ecuacion cuadratica dados sus coeficientes

import math

a=int(input('Ingrese el coeficiente principal '))
b=int(input('Ingrese el segundo coeficiente '))
c=int(input('Ingrese el término constante '))

k=b**2-4*a*c

if k>=0:
    x1=(-b-math.sqrt(k))/(2*a)
    x2=(-b+math.sqrt(k))/(2*a)
    print(f'las raices de su ecuación son {x1} y {x2}')
else:
    print('Las raices son complejas.')


