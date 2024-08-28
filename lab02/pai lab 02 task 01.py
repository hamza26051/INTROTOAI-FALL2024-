def trapezoid():
    a=float(input("enter the side a"))
    b=float(input("enter the side b"))
    h=float(input("etner the height h"))

    area=((a+b)/2)*h

    print(f"the area of trapezoid is {area}")

def parallelogram():
    
    b=float(input("enter the side b"))
    h=float(input("etner the height h"))

    area=b*h

    print(f"the area of parallelogram is {area}")

def volume():
    r=float(input("enter the radius"))
    h=float(input("enter the height"))

    print(f"the volume of the surface is {3.142*r*r*h}")

def area():
    r=float(input("enter the radius"))
    h=float(input("enter the height"))

    print(f"the volume of the surface is {2*3.142*r*(r+h)}")


trapezoid()