import numpy as np 
choice=[2,5,9,10]
number=np.random.choice(choice, (4,4))
identity=np.eye(4)
multiplied=np.multiply(number,identity)
oddnumber=np.arange(1,32,2)
oddarray=np.reshape(oddnumber, (4,4))
multipliedfinalarray=np.add(multiplied,oddarray)
print(multipliedfinalarray)