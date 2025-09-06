import heapq
def heap_sort(iterable):
    heap=[]
    for value in iterable:
        heapq.heappush(heap,value)

    sorted_list=[]
    while heap:
        sorted_list.append(heapq.heappop(heap))
    return sorted_list

nums=[5,3,8,1,2,7]
print("Original:",nums)
print("Heap Sort Asc:", heap_sort(nums))