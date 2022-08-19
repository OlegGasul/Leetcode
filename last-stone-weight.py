import heapq as hq

def lastStoneWeight(stones) -> int:
    if len(stones) == 1:
        return stones[0]
    
    hq._heapify_max(stones)

    while len(stones) > 1:
        a = hq._heappop_max(stones)
        b = hq._heappop_max(stones)
        
        if a != b:
            hq.heappush(stones, a - b)
            hq._heapify_max(stones)

    return stones[0] if len(stones) > 0 else 0



print(lastStoneWeight([2, 7, 4, 1, 8, 1]))