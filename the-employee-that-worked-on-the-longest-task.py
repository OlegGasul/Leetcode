import heapq

def hardestWorker(n: int, logs) -> int:
    time = 0
    hp = []
    heapq.heapify(hp)
        
    for i in range(len(logs)):
        id = logs[i][0]
        end = logs[i][1]
            
        heapq.heappush(hp, [-1 * (end - time), id])
        heapq.heapify(hp)
            
        time = end
            
    minTime, minId = heapq.heappop(hp)
        
    while hp:
        time, id = heapq.heappop(hp)
        if time > minTime:
            break
                
        minId = min(id, minId)
            
    return minId

print(hardestWorker(10, [[0, 3], [2, 5], [0, 9], [1, 15]]))
print(hardestWorker(26, [[1, 1], [3, 7], [2, 12], [7, 17]]))
print(hardestWorker(2, [[0, 10], [1, 20]]))