import heapq

def halveArray(nums) -> int:
    length = len(nums)
        
    total = sum(nums)
    halved = total / 2
        
    heapq._heapify_max(nums)
        
    result = 0
        
    while total > halved:
        value = heapq.heappop(nums)
        total -= value
            
        halvedValue = value / 2
        heapq.heappush(nums, halvedValue)
        
        heapq._heapify_max(nums)
            
        total += halvedValue
        
        result += 1
    
    return result

print(halveArray([5, 19, 8, 1]))