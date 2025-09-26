list1 = [5, 2, 4, 3, 10, 4]
a = []
length = len(list1)
gap = length // 2

while gap > 0 :
    for i in range(gap, length): 
        v = list1[i]
        j = i
        while j >= gap and v <list1[j-gap]:
            list1[j] = list1[j-gap]
            j = j-gap
        list1[j] = j - gap
    gap = gap // 2
print(list1)