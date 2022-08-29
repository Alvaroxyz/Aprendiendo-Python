import numpy as np
import matplotlib.pyplot as plt 

b = np.array([[[[1,2],[3,4]], [[1,2],[3,4]], [[1,2],[5,5]]],
            [[[1,2],[3,4]], [[1,2],[3,4]], [[1,2],[3,4]]],
            [[[1,2],[3,4]], [[1,2],[3,4]], [[1,2],[3,4]]]])


a = [[1,1],[1,1]]

b0 = b[1,2]

d = a*b0


#c = np.zeros((3,3,2,2))

#c[0,1]= a

#print(type(a))
#print(b)
#print(c)

#print(b.shape)
#print(d)

u = list(b)
print(u)



