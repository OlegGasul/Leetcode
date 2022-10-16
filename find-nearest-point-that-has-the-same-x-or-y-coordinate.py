import heapq

def nearestValidPoint(x: int, y: int, points) -> int:
    hp = []
    heapq.heapify(hp)
        
    for i in range(len(points)):
        point = points[i]
        if x == point[0] or y == point[1]:
            heapq.heappush(hp, [abs(x - point[0]) + abs(y - point[1]), i])
                
    if not hp:
        return -1
        
    minDist, minIndex = heapq.heappop(hp)
        
    while hp:
        dist, index = heapq.heappop(hp)
        if dist > minDist:
            break
        minIndex = min(minIndex, index)
            
    return minIndex

print(nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
print(nearestValidPoint(3, 4, [[3, 4]]))