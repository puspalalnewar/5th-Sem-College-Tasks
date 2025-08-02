# Find the nth Fibonacci number using recursion. The value of n should be taken as input.

def nthFib(num) :
    if num==0 :
        return 1
    if(num == 1) :
        return 1
    return nthFib(num-1) + nthFib(num-2)

print(nthFib(5))