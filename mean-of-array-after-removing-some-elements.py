import math
import heapq

def trimMean(arr):
    heap = []
    heapq.heapify(heap)

    length = len(arr)
    total = 0
    
    for i in range(length):
        total += arr[i]
        heapq.heappush(heap, arr[i])
        

    count = math.floor(length * 0.05)

    return (total - sum(heapq.nsmallest(count, heap)) - sum(heapq.nlargest(count, heap))) / (length - 2 * count)


# print(trimMean([1, 2, 12, 2, 2, 4, 2, 2, 2, 2, 7, 2, 2, 2, 3, 2, 2, 2, 2, 3]))
print(trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))