import heapq

def findClosestElements(arr, k: int, x: int):
    length = len(arr)
    if length <= k:
        return arr

    left = 0
    right = length - 1

    while left <= right:
        index = left + (right - left) // 2

        if arr[index] == x:
            break
        
        if arr[index] > x:
            right = index - 1
        else:
            left = index + 1

    print('index = ' + str(index))

    heap = []

    for i in range(index, min(index + k, length - 1)):
        heapq.heappush(heap, arr[i])
        heapq.heapify(heap)

    for i in reversed(range(max(index - k, 0), index)):
        heapq.heappush(heap, arr[i])
        heapq.heapify(heap)

    return heapq.nsmallest(k, heap)
    

# print(findClosestElements([1, 2, 3, 4, 5], 4, 3))
# print(findClosestElements([1, 2, 3, 9, 10], 2, 4))
# print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 10))
print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))