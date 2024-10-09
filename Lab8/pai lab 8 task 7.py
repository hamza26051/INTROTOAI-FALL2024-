import numpy as np 
number1=np.random.rand(1000)
average=np.average(number1)
variance=np.var(number1)
std=np.std(number1)

with open("textfile.txt", "w") as file:
  file.write(f"Average{average}, variance :{variance}, standard deviation:{std}")



