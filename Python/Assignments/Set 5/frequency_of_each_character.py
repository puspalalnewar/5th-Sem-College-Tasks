# Find the frequency of occurrence of each character in a given string.

def PresentinUniqueArray(uniqueArr,ch):
    for i in range(len(uniqueArr)):
        if uniqueArr[i]==ch:
            return True
    return False

#MAIN
str = input("Enter string : ")
uniqueArr = []
freqArr = []

# taking unique items to a new array
uniqueArr.append(str[0])
for i in range(len(str)):
    if not PresentinUniqueArray(uniqueArr,str[i]):
        uniqueArr.append(str[i])
print("unique array : ",uniqueArr)

#filling up the freqArray
for i in range(len(uniqueArr)):
    count=0
    for j in range(len(str)):
        if uniqueArr[i]==str[j]:
            count+=1
    freqArr.append(count)


print("\tFrequencies : ")
for i in range(len(uniqueArr)):
    print(uniqueArr[i]," --> ",freqArr[i]," times")