#  Input a string and two patterns pattern1 and pattern2. Find all occurrences of pattern1 and replace them by pattern2.


def replaceByPattern(str,pattern1,pattern2):
    slicedList = str.split(pattern1)
    newStr= ""
    noOfel = len(slicedList)
    for i in range(noOfel):
        newStr+=slicedList[i]
        if i<noOfel-1:
            newStr+=pattern2
    print("After replacing \"",pattern1,"\" by \"",pattern2,"\" : ",newStr)



#main
str = input("Enter string : ")
pattern1 = input("Enter pattern 1 : ")
pattern2 = input("Enter pattern 2 : ")
replaceByPattern(str,pattern1,pattern2)