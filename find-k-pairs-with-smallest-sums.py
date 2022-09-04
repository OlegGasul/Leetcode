import heapq

def kSmallestPairs(nums1, nums2, k: int):
    queue = []
    heapq.heapify(queue)
        
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            heapq.heappush(queue, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
            heapq.heapify(queue)
                
    result = []
        
    for i in range(min(k, len(queue))):
        result.append(queue[i][1])
    
    return result

print(kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(kSmallestPairs([1, 2], [3], 3))