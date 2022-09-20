import heapq

def minCostConnectPoints(points) -> int:
    edges = []
    
    length = len(points)

    for i in range(length - 1):
        for j in range(i + 1, length):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))
    
    heapq.heapify(edges)

    parent = [i for i in range(length)]

    def find(k):
        if parent[k] != k:
            parent[k] = find(parent[k])
        return parent[k]

    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        if s1 != s2:
            parent[s2] = parent[s1]
            return True

        return False

    result = 0
    count = 0
    while count < length - 1:
        dist, x, y = heapq.heappop(edges)

        if union(x, y):
            result += dist
            count += 1

    return result
    
print(minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))