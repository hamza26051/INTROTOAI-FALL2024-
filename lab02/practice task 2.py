def calculatearea():
    width=float(input("enter the width"))
    length=float(input("enter the length"))

    area=length*width

    return area

print(f"the area is {calculatearea()}")