# Input a string and a pattern and delete all occurrences of the pattern from the string.

def removePattern(str,pattern):
    slicedList =[]
    newStr = "" 
    slicedList = str.split(pattern)
    for subString in slicedList:
        newStr+=subString
    print("After removing the pattern \"",pattern,"\" : ",newStr)
    
#Main
str = input("Enter String : ")
pattern = input("Enter pattern : ")

removePattern(str,pattern)
