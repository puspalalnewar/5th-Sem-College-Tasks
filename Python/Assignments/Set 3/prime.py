# checking prime or not
num = int(input("Enter number : "))
count = 0;
for i in range(1,num):
    if num%i==0:
        count+=1
if count>2:
    print(num," is NOT a prime number")
else :
    print(num," is a PRIME number")