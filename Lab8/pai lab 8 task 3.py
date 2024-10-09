import numpy as np 

number=np.arange(1,19)
evennumber=number[number%2==0]
array=evennumber.reshape((3,3))
multiplyarray=np.multiply(array,4)
identity=np.eye(3)
product=np.multiply(multiplyarray,identity)
print(product)