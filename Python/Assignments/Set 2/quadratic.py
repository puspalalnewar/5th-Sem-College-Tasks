# Solve a given quadratic equation. (Without imaginary root).
import math

#main
a,b,c=input("Arrange the equation in the standard form\n\n\tax^2+bx+c=0\n\nEnter values of the coefficients repectively (seperated by commas) : ").split(",")
a,b,c = int(a), int(b), int(c)

discriminant=b**2-4*a*c

if a==0:
    print("value of a cannot be Zero!")
elif(discriminant<0):
    print("Roots are IMAGINARY !")
elif(discriminant==0):
    print(f"Roots are {(-1*b)/(2*a)},{(-1*b)/(2*a)}")
else:
    print(f"Roots are {((-1*b)+math.sqrt(discriminant))/(2*a)},{((-1*b)-math.sqrt(discriminant))/(2*a)}")