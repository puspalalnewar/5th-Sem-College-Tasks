# star hourglass pattern

"""

*******
 ***** 
  *** 
   *
  ***  
 ***** 
*******

"""

# AUKAD nai :(


rows = 7
n = rows // 2 + 1

# Top half
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))

# Bottom half
for i in range(2, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))