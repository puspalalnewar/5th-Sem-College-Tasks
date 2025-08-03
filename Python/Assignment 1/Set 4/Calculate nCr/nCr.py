n = int(input("Enter the val of n : "))
r = int(input("Enter the val of r : "))

def findFactorial(num) :
    fact = 1
    if num == 0 :
        return 1
    for i in range(1, num+1) :
        fact = fact * i
    return fact

def cal_nCr(n, r) :
    if n < r :
        return 0
    n_Factorial = findFactorial(n)
    r_Fcatorial = findFactorial(r)
    n_minus_r_factorial = findFactorial(n-r)
    
    nCr_val = n_Factorial // (r_Fcatorial * n_minus_r_factorial)
    return nCr_val

print("nCr : ", cal_nCr(n, r))