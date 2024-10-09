import numpy as np 

number=np.arange(1,19)
oddnumber=number[number%2!=0]
print(oddnumber)
array=oddnumber.reshape((3,3))
print(array)