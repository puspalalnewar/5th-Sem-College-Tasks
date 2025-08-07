# Input a string and a pattern and count the occurrences of the pattern in the string.

def patternCount(str,pattern):
    slicedStr = []
    lengthOfpattern = len(pattern) # so that i don't need to call len() again
    for i in range(len(str)-1):
        slicedStr.append(str[i:i+lengthOfpattern])
        i+=1
    count = 0
    for subString in slicedStr:
        if(pattern==subString):
            count+=1
    return count

#main
str = input("Enter string : ")
pattern = input("Enter pattern to search : ")


print(pattern," appeared : ",patternCount(str,pattern)," times")

