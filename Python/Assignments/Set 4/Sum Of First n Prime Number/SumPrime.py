num = int(input("Enter your number : "))

# ! Functuon to check Prime number
def isPrime(num) :
    if num == 1 :
        return False
    for i in range (2, num) :
        if num % i == 0 :
            return False
    return True    

# ! Function for Sum of first n prime number
def sumOfPrimeNum(num) :
    sum = 0
    for i in range(2, num+1) :
        if isPrime(i) :
            sum += i
    return sum

print("Sum of first n prime number : " , sumOfPrimeNum(num))