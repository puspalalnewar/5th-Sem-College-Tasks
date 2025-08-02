#Print the sum of natural numbers up to n using recursion.

n = int(input("Enter your number : "))

def sum_of_natural_num(num) :
    if num < 0 :
        return 0
    else :
        return num + sum_of_natural_num(num - 1)

print(sum_of_natural_num(n))