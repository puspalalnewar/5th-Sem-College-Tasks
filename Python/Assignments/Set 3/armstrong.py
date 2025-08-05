# checking armstrong number
num = int(input("Enter a number : "))

temp = num
digits = 0

while temp!=0:
    digits+=1
    temp//=10

temp = num

sum = 0

while temp!=0:
    sum+=(temp%10)**digits
    temp//=10

if sum==num:
    print(num, " is a ARMSTRONG number")
else:
    print(num, " is NOT a amrstrong number")