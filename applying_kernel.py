import numpy as np  
import matplotlib.pyplot as plt 


#Funciones

def dimensiones_convolucion(A, k, sh, sv):
    """Calcula las filas y las columnas de KA 
    y retorna una lista con los datos."""
    dk = k.shape
    dim_c = int(np.floor(((A.shape[1]-dk[1])/sh)+1))
    dim_f = int(np.floor(((A.shape[0]-dk[0])/sv)+1))
    r = [dim_f, dim_c]
    return r


def convolucion_capa(A,k,sh,sv):
    """Toma una capa y entrega la convolución con el kernel
    """
    dk = k.shape 
    d = dimensiones_convolucion(A,k,sh,sv)
    B = np.zeros(d)
    for i in range(d[0]):
        for j in range(d[1]):
            B[i,j] = sum(sum(A[i*sv:i*sv+dk[1],j*sh:j*sh+dk[0]]*k))
    return B


def ensambla_convolucion_canales(canal_1,canal_2,canal_3):
    """Ensambla cada uno de los canales una vez hecha la convolución
    para cada uno de ellos"""
    d = canal_1.shape
    KA = np.zeros((d[0],d[1],3))
    for i in range(d[0]):
        for j in range(d[1]):
            KA[i,j] = np.array([canal_1[i,j],canal_2[i,j],canal_3[i,j]])
    return KA



#Instrucciones

A = plt.imread('./Archivos/marilyn.png')

kh = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kv = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kl = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
kb = (-1/9)*np.ones((3,3))

k = kl
sh = 1
sv = 1

c1 = convolucion_capa(A[:,:,0], k, sh, sv)
c2 = convolucion_capa(A[:,:,1], k, sh, sv)
c3 = convolucion_capa(A[:,:,2], k, sh, sv)

ka = ensambla_convolucion_canales(c1, c2, c3)

plt.imshow(ka)
plt.show()
