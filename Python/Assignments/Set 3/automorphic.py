# automorphic numbers : 5->25, 6->36,...

def noOfdigits(n):
    count = 0
    while n!=0:
        count+=1
        n//=10
    return count

def automorphic(n):
    digits = noOfdigits(n)
    if n%10**digits==(n**2)%10**digits:
        return True
    else:
        return False

# main part
choice = int(input("\t\tChoose\n\n1. Check a single number\n2. print all the numbers in a range\n\nEnter choice : "))

if choice == 1:
    n = int(input("Enter number : "))
    if automorphic(n):
        print(n," is AUTOMORPHIC")
    else : print(n," is NOT an automorphic number")
    
elif choice == 2:
    n = int(input("Enter the last number (1,?) : "))
    for i in range(1,n+1):
        if automorphic(i):
            print(i," -> ",i**2)
else : 
    print("Invalid Input")