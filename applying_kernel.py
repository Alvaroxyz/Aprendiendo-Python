import numpy as np 
import matplotlib.pyplot as plt 


#Funciones

def dimKA(A, k, sh, sv):
    """Calcula las filas y las columnas de KA y retorna una tupla con los datos."""
    dk = k.shape[0]
    dim_c = int(np.floor(((A.shape[1]-dk)/sh)+1))
    dim_f = int(np.floor(((A.shape[0]-dk)/sv)+1))
    r = (dim_f, dim_c)
    return r

def mA(A,k,sh,sv):
    """Parcela una capa y retorna la matriz de matrices para multiplicar por el kernel."""
    dk = k.shape
    d = dimKA(A,k, sh, sv)
    B = np.zeros(d,dtype=ndarray)
    for i in range(d[0]+1):
        for j in range(d[1]+1):
            B[i,j] = np.array(A[i*sh:dk[0]+1,j*sv:dk[1]+1])
    return B

def mcon(B,k):
    """Calcula el producto tensorial de cada entrada de la convolución
    de una capa con el kerenel y retorna la capa con los productos 
    en cada entrada.
    """
    t = B.shape
    for i in range(t[0]+1):
        for j in range(t[1]+1):
            #producto tensorial
            B[i,j] = sum(B[i,j]*k)
    return B

def conv(cA, k,sh,sv):
    """Cálculo directo de la convolución para un canal de A digamos cA
    a partir de A, k, sh, sv.
    """
    v0 = mA(cA,k,sh,sv)
    v1 = mcon(v0,k)
    return v1

def KA(B1, B2, B3):
    """ Ensambla los tres canales ya hecha la convolución"""
    Ka = np.array([B1,B2,B3])
    return Ka

def img2(A,k,sh,sv):
    A0 = A[:,:,0]
    A1 = A[:,:,1]
    A2 = A[:,:,2]

    B0 = conv(A0,k,sh,sv)
    B1 = conv(A1,k,sh,sv)
    B2 = conv(A2,k,sh,sv)

    sol = KA(B0,B1,B2)
    return sol


#Instrucciones

marilyn = plt.imread('./Archivos/marilyn.png')






kh = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kv = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kl = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
kb = (-1/9)*np.ones((3,3))

k = kh
sh = 1
sv = 1
#sh = int(input('Sancada horizontal: '))
#sv = int(input('Sancada vertical: '))


