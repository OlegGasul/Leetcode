import heapq

def findMaximizedCapital(k: int, w: int, profits, capital) -> int:
    heap = []
    projects = sorted(zip(profits, capital), key=lambda a: a[1])
    
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][1] <= w:
            heapq.heappush(heap, -projects[i][0])
            i += 1
        if heap:
            w -= heapq.heappop(heap)
    return w

print(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))