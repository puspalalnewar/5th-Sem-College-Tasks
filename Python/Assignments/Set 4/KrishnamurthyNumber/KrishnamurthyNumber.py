# A Krishnamurthy number (also called a Strong number or Peterson number) is a special number in mathematics whose sum of the factorials of its digits is equal to the original number itself.
# Example : 1! + 4! + 5! = 1 + 24 + 120 = 145

# Function for find factorial
def findFactorial(num) : 
    fact = 1
    if num == 0 :
        return 1
    for i in range(1, num+1) :
        fact = fact * i
    return fact

# Function for find krishnamurthy number
num = int(input("Enter your number : "))
store = num
def isKrishnamurthy(num) :
    sum = 0
    while num > 0 :
        lastDig = num % 10
        sum += findFactorial(lastDig)
        num = num // 10
    return sum

if isKrishnamurthy(store) == store :
    print("True")
else : 
    print("False")
    
    
