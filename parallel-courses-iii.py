from collections import defaultdict
from functools import lru_cache

class Solution:
    def minimumTime(self, n: int, relations, time) -> int:
        graph = defaultdict(list)
        for u, v in relations:
            graph[v].append(u)

        @lru_cache(None)
        def dp(node):
            return time[node - 1] + max([dp(child) for child in graph[node]] + [0])

        return max(dp(i) for i in range(1, n + 1))

solution = Solution()
print(solution.minimumTime(9, [[2, 7], [2, 6], [3, 6], [4, 6], [7, 6], [2, 1], [3, 1], [4, 1], [6, 1], [7, 1], [3, 8], [5, 8], [7, 8], [1, 9], [2, 9], [6, 9], [7, 9]], [9, 5, 9, 5, 8, 7, 7, 8, 4]))
print(solution.minimumTime(1, [], [1]))
print(solution.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))
print(solution.minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))