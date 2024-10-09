import numpy as np 

number=np.arange(21,50)
evennumber=number[number%2==0]
array=np.array(evennumber)
print(array)