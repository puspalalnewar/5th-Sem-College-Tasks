# Input a limit n and print all twin prime numbers up to n.

def isPrime(a) :
    if a <= 1 :
        return False
    for i in range (2, a) :
        if a % i == 0 :
            return False
    return True

num = int(input("Enter your number : "))
list = []
for i in range(1, num+1) :
    if isPrime(i) == True:
        list.append(i)
list_tuple = tuple(list)
print(list_tuple)

def twinPrime(list_tuple) :
    for i in range(len(list_tuple)-1) :
        if list_tuple[i+1] - list_tuple[i] == 2 :
            print(list_tuple[i], list_tuple[i+1])
            
twinPrime(list_tuple)