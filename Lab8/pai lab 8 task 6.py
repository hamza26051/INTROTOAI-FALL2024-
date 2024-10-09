import numpy as np 
number1=np.arange(1,16)
number2=np.arange(1,7)
array1=number1.reshape(5,3)
array2=number2.reshape(3,2)
multiply=np.dot(array1,array2)
print(multiply)
