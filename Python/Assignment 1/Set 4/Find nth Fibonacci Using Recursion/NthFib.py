# Find the nth Fibonacci number using recursion. The value of n should be taken as input.

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0  # By common definition, F(1) = 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take input from the user
n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")