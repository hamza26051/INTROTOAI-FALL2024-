number1=float(input("enter your first number"))
number2=float(input("enter your second number"))
operator=input("enter the operator(+ for addition, - for subtraction, * for multiplication, / for division)")
if operator =="+":
    result=number1-(-number2)
elif operator =="-":
    result=number1-number2
elif operator =="*":
    result=number1*number2
elif operator =="/":
    result=number1/number2
else:
    print("enter valid operator")
print(f"the result is {result}")