import heapq

class Solution:
    def wallsAndGates(self, rooms) -> None:
        empty = float('inf')
        rows = len(rooms)
        cols = len(rooms[0])

        pq = []
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    heapq.heappush(pq, [0, i, j])

        def dfs(i, j, dist):
            if i < 0 or i >= rows:
                return
            if j < 0 or j >= cols:
                return
            
            if rooms[i][j] <= dist + 1:
                return
            
            rooms[i][j] = dist + 1
            heapq.heappush(pq, [dist + 1, i, j])
        
        while pq:
            dist, i, j = heapq.heappop(pq)

            dfs(i, j + 1, dist)
            dfs(i + 1, j, dist)
            dfs(i, j - 1, dist)
            dfs(i - 1, j, dist)

solution = Solution()
rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647,-1,2147483647,-1],
    [0, -1, 2147483647, 2147483647]]
solution.wallsAndGates(rooms)
assert rooms == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
