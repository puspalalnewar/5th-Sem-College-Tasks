import math
# ! Q7. Compute the telephone bill for Mr. X as per the call rates given below:
    
#     Base tariff = 250
#     1st 100 calls   @Rs.  0.2
#     Next 100 calls  @ Rs. 0.3
#     Remaining calls @ Rs. 0.5

# ! Q8. Solve a given quadratic equation. (Without imaginary root).

# ax^2 + bx + c = 0

a,b, c = map(int, input("Enter value of a, b, c seperated via space : ").split(" "))
print(a,b,c)

# x = -b + rootover(b^2 - 4ac) / 2a

if b**2 - 4 * a * c == 0 :
    print("Roots are Imaginary")
else :
    print(f"Roots of equations are : ({(-b + math.sqrt(b**2 - 4*a*c)) / (2*a)}, {(-b - math.sqrt(b**2 - 4*a*c)) / (2*a)})")