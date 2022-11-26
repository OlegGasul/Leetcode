class Solution:
    def minArea(self, image, x: int, y: int) -> int:
        rows = len(image)
        cols = len(image[0])

        bounds = [x, y, x, y]
        visited = set()

        def dfs(i, j):
            if (i, j) in visited or i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or image[i][j] != "1":
                return
            
            visited.add((i, j))
            bounds[0] = min(bounds[0], i)
            bounds[1] = min(bounds[1], j)
            bounds[2] = max(bounds[2], i)
            bounds[3] = max(bounds[3], j)

            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)

        dfs(x, y)

        return (bounds[2] - bounds[0] + 1) * (bounds[3] - bounds[1] + 1)

solution = Solution()
assert solution.minArea([["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 2) == 6
assert solution.minArea([["1"]], 0, 0) == 1