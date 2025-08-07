# Input a string and delete all consecutive occurrences of characters.


#main
str = input("Enter string : ")
str2 = ""
for i in range(len(str)):
    if i==len(str)-1 or str[i]!=str[i+1] :
        str2+=str[i]
print(str2)
        