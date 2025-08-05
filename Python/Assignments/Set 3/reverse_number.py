# reversing a number 

num = int(input("Enter number (avoid the digit 0) : "))

temp = num
sum = 0

def noOfdigits(n):
    count = 0;
    while n!=0:
        count+=1
        n//=10
    return count
# while loop
while temp!=0:
    rem = temp%10
    sum = sum*10+rem
    temp//=10
print(num," --> ",sum)


# for loop
sum = 0
temp = num
digits = noOfdigits(num)
for i in range(1,digits+1,1):
    rem = temp%10
    sum = sum*10+rem
    temp//=10
print(num," --> ",sum)