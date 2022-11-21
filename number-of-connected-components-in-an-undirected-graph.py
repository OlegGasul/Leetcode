from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges) -> int:
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        groups = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for v in graph[node]:
                dfs(v)

        for node in range(n):
            if node in visited:
                continue
            
            groups += 1
            dfs(node)

        return groups

solution = Solution()
assert solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1