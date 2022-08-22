import heapq
import math

def minStoneSum(piles, k: int) -> int:
    heapq._heapify_max(piles)
    
    while k > 0:
        value = heapq._heappop_max(piles)
        value = math.ceil(value / 2)
        
        heapq.heappush(piles, value)
        heapq._heapify_max(piles)
        
        k -= 1

    return sum(piles)

print(minStoneSum([5, 4, 9], 2))
print(minStoneSum([4, 3, 6, 7], 3))