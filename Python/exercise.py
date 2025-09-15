import math
# ! Q7. Compute the telephone bill for Mr. X as per the call rates given below:
    
#     Base tariff = 250
#     1st 100 calls   @Rs.  0.2
#     Next 100 calls  @ Rs. 0.3
#     Remaining calls @ Rs. 0.5

# ! Q8. Solve a given quadratic equation. (Without imaginary root).

# ! Q9. Make Star Diamond

#             *     
#           * * *
#         * * * * *
#       * * * * * * *
#         * * * * *
#           * * *
#             *

# row = 5
# for i in range (1, row+1) :
#     print(" " * (row - i) + ("* ") * i)
# # Lower part of the diamond
# for i in range(row - 1, 0, -1):
#     print(" " * (row - i) + "* " * i)

# ! Q10. Make star hourglass

#         * * * * * * *
#           * * * * *
#             * * *
#               *
#             * * *
#           * * * * *
#         * * * * * * *

# row = 4
# # For Upper Part
# for i in range(row, 0, -1) :
#     print(" " * (row-i) + "* " * i)
# #For lower part
# for i in range(2, row+1) :
#     print(" " * (row-i) + "* " * i)

# ! Q11. Input two numbers and find their hcf and lcm
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2 : "))
# hcf = math.gcd(num1, num2)
# lcm = (num1 * num2) // hcf
# print(f"LCM : {lcm}\nHCF : {hcf}")