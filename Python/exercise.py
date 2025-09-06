# Merge Sort
def merge_sort(arr, lb, ub) :
    if lb < ub :
        mid = (lb + ub) // 2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, ub)
        simple_merge(arr, lb, mid, ub)

# Simple merge
def simple_merge(arr, lb , mid, ub) :
    aux = [0] * len(arr)
    i, j, k = lb, mid+1, lb
    while i <= mid and j <= ub :
        if arr[i] < arr[j] :
            aux[k] = arr[i]
            i = i+1
        else :
            aux[k] = arr[j] 
            j = j+1
        k = k+1
    while i <= mid :
        aux[k] = arr[i]    
        i = i+1
        k = k+1
    while j <= ub :
        aux[k] = arr[j]
        j = j+1
        k = k+1
    for idx in range(lb, ub+1) :
        arr[idx] = aux[idx]    

# Main
arr = [50, 41 , 20, -1, 0, 7]
# for i in range (len(arr)) :
#     arr[i] = int(arr[i])
merge_sort(arr, 0, len(arr)-1)
print(arr)