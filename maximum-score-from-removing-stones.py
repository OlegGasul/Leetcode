import heapq

def maximumScore(a: int, b: int, c: int) -> int:
    heap = [a, b, c]
    heapq._heapify_max(heap)

    result = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        
        if a > 1:
            heapq.heappush(heap, a - 1)
        
        if b > 1:
            heapq.heappush(heap, b - 1)
        
        heapq._heapify_max(heap)
        
        result += 1

    return result



print(maximumScore(2, 4, 6))
print(maximumScore(4, 4, 6))
print(maximumScore(1, 8, 8))
print(maximumScore(6, 2, 1))