import heapq

#Create  an empty heap
heap=[]

#push values
heapq.heappush(heap,5)
heapq.heappush(heap,3)
heapq.heappush(heap,8)
heapq.heappush(heap,1)

print("Heap (internal list): ",heap)
print("Pop smallest: ", heapq.heappop(heap))
print("Pop next smallest", heapq.heappop(heap))