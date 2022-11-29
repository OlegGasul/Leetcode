class Solution:
    def minDistance(self, height: int, width: int, tree, squirrel, nuts) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        result = 0
        d = float('-inf')
        for n in nuts:
            result += distance(n, tree) * 2
            d = max(d, distance(n, tree) - distance(n, squirrel))

        return result - d

solution = Solution()
assert solution.minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2,5]]) == 12
assert solution.minDistance(1, 3, [0, 1], [0, 0], [[0, 2]]) == 3