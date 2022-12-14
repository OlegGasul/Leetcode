from collections import Counter

class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        parent = [-1] * n

        def find(node):
            if parent[node] == -1:
                return node
            return find(parent[node])
        
        def union(a, b):
            x = find(a)
            y = find(b)
            if x != y:
                parent[x] = y

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    union(i, j)

        return Counter(parent)[-1]

solution = Solution()
assert solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3