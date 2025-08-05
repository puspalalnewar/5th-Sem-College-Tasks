# finding HCF and LCM 
num1,num2 = input("Enter two number (seperated by commas) : ").split(",")
num1,num2 = int (num1), int(num2)
larger = num1 if num1>num2 else num2
smaller = num1 if num1<num2 else num2
i = 1
while larger*i%smaller!=0:
    i+=1
print(f"LCM of {num1} and {num2} is : {larger*i}\nHCF of {num1} and {num2} is : {(num1*num2)//(larger*i)}")