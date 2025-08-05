# Fibonacci Series

def fiboUptoN(n):
    fir = 0
    sec = 1
    temp = 0
    print("\nFibo upto ",n,"th term : ",end=" ")
    for i in range(0,n):
        print(fir, end=' ')
        temp = fir + sec
        fir = sec
        sec = temp

def nthFibo(n): 
    fir=0
    sec=1
    temp = 0
    for i in range(1,n):
        temp = fir+sec
        fir = sec
        sec = temp
    print("The ",n,"th number is Fibonacci series is : ",fir)
    
# main part
conti = "y"
while  conti != "n":
    mode = int(input("\n\t\tOption\n\n1. Print UPTO nth Fibonacci series\n2. Print the Nth Fibonacci series\n\nEnter choice : "))
    if mode<1 or mode>2:
        print("Invalid Choice")
    elif mode==1:
        n=int(input("Enter no of terms : "))
        if n<=0:
            print("no of terms cannot be <= 0")
        else : fiboUptoN(n)
    elif mode==2:
        n=int(input("Enter the term no. : "))
        if n<=0:
            print("No of terms cannot be <= 0")
        else : nthFibo(n)
    conti = input("\nContinue? (y/n) : ")