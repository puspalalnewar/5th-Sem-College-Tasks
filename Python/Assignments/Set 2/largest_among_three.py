num1, num2, num3 = input("Enter three numbers (seperated by commas) : ").split(",")
num1, num2, num3 = float(num1), float(num2), float(num3)
if num1>num2 and num1>num3:
    print("largest : ",num1)
elif num2>num1 and num2>num3:
    print("largest : ",num2)
else:
    print("largest ; ",num3)
if num1<num2 and num1<num3:
    print("smallest : ",num1)
elif num2<num3 and num2<num1:
    print("smallest : ",num2)
else:
    print("smallest : ",num3)