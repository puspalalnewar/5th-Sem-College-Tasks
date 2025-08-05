# checking leap year
year = int(input("Enter year : "))
if year % 4 ==0 and year%100 !=0:
    print(year,"is a LEAP year")
elif year%400==0:
    print(year," is a LEAP year")
else : 
    print(year," is NOT a leap year")
