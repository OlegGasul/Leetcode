import heapq

def sortPeople(names, heights):
    dp = []
    
    for i in range(len(names)):
        heapq.heappush(dp, (heights[i], names[i]))
        heapq.heapify(dp)
    
    result = []
    while dp:
        result.insert(0, heapq.heappop(dp)[1])
            
    return result

print(sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))