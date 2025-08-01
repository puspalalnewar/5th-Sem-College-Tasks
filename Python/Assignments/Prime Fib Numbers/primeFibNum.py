# ! Input a limit n and print all prime fibonacci numbers up to n using a user defined function prime() which returns a 1 if the argument is a prime or else 0.


input = int(input("Enter your number : "))

# ! Functuon to check Prime number
def isPrime(num) :
    if num == 1 :
        return 0
    for i in range (2, num) :
        if num % i == 0 :
            return 0
    return 1  
    

    