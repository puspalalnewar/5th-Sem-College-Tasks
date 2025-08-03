# ! Input a limit n and print all prime fibonacci numbers up to n using a user defined function prime() which returns a 1 if the argument is a prime or else 0.

# ! Functuon to check Prime number
def isPrime(num) :
    if num == 0 :
        return 0
    if num == 1 :
        return 0
    for i in range (2, num) :
        if num % i == 0 :
            return 0
    return 1  
    
n = int(input("Enter how many Fibonacci numbers you want: "))

a, b = 0, 1
fib_list = []

for _ in range(n):
    fib_list.append(a)
    a, b = b, a + b

fib_tuple = tuple(fib_list)

print("Fibonacci series as tuple:")
print(fib_tuple)

for i in range(len(fib_tuple)) :
    if isPrime(fib_tuple[i]) == 1 :
        print(fib_tuple[i])  