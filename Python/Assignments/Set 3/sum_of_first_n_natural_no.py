# Print the sum of natural numbers up to n using recursion

def sum(n):
	if n<=0:
		print(n,"is not a natural number")
		return	 
	if n==1:
		return 1
	return n+sum(n-1)

#MAIN
n = int(input("Enter number : "))

print("sum till ",n," : ",sum(n))