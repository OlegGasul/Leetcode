import heapq as hq

def maximumProduct(nums, k: int) -> int:
    heap = []
    hq.heapify(heap)
    for x in nums:
        hq.heappush(heap, x)

    for i in range(k):
        value = hq.heappop(heap)
        value += 1
        hq.heappush(heap, value)

    result = 1
    for x in heap:
        result *= x

    print(heap)

    return result



# print(maximumProduct([0, 4], 5))
# print(maximumProduct([6, 3, 3, 2], 2))
print(maximumProduct([24, 5, 64, 53, 26, 38], 54))