def merge_sort(arr, lb, ub) : 
    if lb < ub : 
        mid = (lb + ub) // 2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, ub)
        simple_merge(arr, lb, mid, ub)
        
def simple_merge(arr, lb, mid, ub) : 
    aux = [0]*len(arr)
    i, j, k = lb, mid+1, lb
    while i <= mid and j <= ub :
        if arr[i] < arr[j] : 
            aux[k] = arr[i]
            i += 1
        else:
            aux[k] = arr[j]
            j += 1
        k+=1
    while i<=mid : 
        aux[k] = arr[i]
        i+=1
        k+=1
    while j<=ub:
        aux[k] = arr[j]
        j+=1
        k+=1
    for idx in range(lb, ub+1) : 
        arr[idx] = aux[idx]    

# Main
arr = []
arr= input("Enter arr element separated by space : ").split(" ")
for i in range (len(arr)) :
    arr[i] = int(arr[i])
merge_sort(arr, 0, len(arr)-1)
print(arr)